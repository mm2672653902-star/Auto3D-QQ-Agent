from fastapi import FastAPI, Request
from agent_core.orchestrator import AgentOrchestrator
import uvicorn

app = FastAPI(title="Auto3D QQ Agent API")
orchestrator = AgentOrchestrator()

@app.post("/qq_webhook")
async def handle_qq_message(request: Request):
    """
    接收 QQ 机器人框架（如 NoneBot 或 go-cqhttp）转发过来的消息
    """
    payload = await request.json()
    user_message = payload.get("raw_message", "")
    user_id = payload.get("sender", {}).get("user_id", "")

    if not user_message:
        return {"status": "ignored"}

    print(f"收到来自 {user_id} 的指令: {user_message}")
    
    # 触发 Agent 工作流
    reply_content = orchestrator.process_task(user_message)
    
    # 这里通常会调用 QQ API 将 reply_content 发送回去
    # 示例直接返回 JSON
    return {
        "action": "send_msg",
        "params": {
            "user_id": user_id,
            "message": reply_content
        }
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
