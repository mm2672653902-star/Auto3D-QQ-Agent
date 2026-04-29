# Auto3D-QQ-Agent 🤖✨

基于多模型 API 与 Agent 架构构建的自动化代码辅助机器人，专注于 3D 渲染（Three.js）和自动化脚本的生成与调试。

## 🌟 核心特性
- **多 Agent 协同**：包含意图识别、长链推理与代码生成多个子 Agent。
- **无缝接入**：通过 Webhook 挂载至 QQ 机器人，实现移动端随时随地的开发灵感记录与代码生成。
- **3D 粒子专家**：内置针对 Three.js 粒子系统的深度优化 Prompt，可根据自然语言直接生成带参数配置的闭环代码。

## 🚀 快速开始

1. 克隆本仓库
2. 安装依赖：`pip install -r requirements.txt`
3. 配置环境变量 `.env`，填入你的模型 API Key (支持 DeepSeek, 准备接入 MiMo)
4. 运行服务：`uvicorn main:app --host 0.0.0.0 --port 8080`
