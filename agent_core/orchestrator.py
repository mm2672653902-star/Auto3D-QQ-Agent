import os
from openai import OpenAI
from .prompts import INTENT_SYSTEM_PROMPT, THREEJS_EXPERT_PROMPT

class AgentOrchestrator:
    def __init__(self):
        # 兼容标准 OpenAI 接口的多模型调用，随时可替换为 MiMo API
        self.client = OpenAI(
            api_key=os.getenv("MODEL_API_KEY", "your_default_api_key"),
            base_url=os.getenv("MODEL_BASE_URL", "https://api.deepseek.com/v1")
        )

    def _call_llm(self, system_prompt: str, user_prompt: str) -> str:
        try:
            response = self.client.chat.completions.create(
                model="deepseek-chat", # 评估通过后计划替换为 MiMo
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.7
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Agent 节点调用异常: {str(e)}"

    def process_task(self, user_input: str) -> str:
        # Step 1: 意图识别 Agent
        print("-> 启动意图识别 Agent...")
        intent = self._call_llm(INTENT_SYSTEM_PROMPT, user_input).strip()
        
        # Step 2: 任务分发与长链执行
        if "3D_RENDER" in intent:
            print("-> 触发 3D 渲染专家 Agent...")
            return self._call_llm(THREEJS_EXPERT_PROMPT, user_input)
        elif "CODE_DEBUG" in intent:
            print("-> 触发 Debug 分析 Agent...")
            return self._call_llm("你是一个资深后端工程师，请帮用户分析报错并给出重构建议。", user_input)
        else:
            return "收到你的日常指令，正在闲聊模式待机中..."
