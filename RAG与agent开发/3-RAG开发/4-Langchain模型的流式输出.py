# # langchain_community
# import os
# from langchain_community.llms.tongyi import Tongyi
#
# model = Tongyi(model="qwen-max", api_key=os.environ.get("DASHSCOPE_API_KEY"))
#
# # 用stream访问模型
# response = model.stream("你是谁?")
# for chunk in response:
#     print(chunk, end="", flush=True)
#
#
#
# # langchain_ollama
# from langchain_ollama import OllamaLLM
#
# model = OllamaLLM(model="deepseek-r1:1.5b")
#
# # 用stream访问模型
# response = model.stream("你是谁？")
# for chunk in response:
#     print(chunk, end="", flush=True)
#



# 优化版
import os
from langchain_community.llms.tongyi import Tongyi

def create_model():
    api_key = os.getenv("DASHSCOPE_API_KEY")
    if not api_key:
        raise ValueError("请先设置环境变量 DASHSCOPE_API_KEY")

    return Tongyi(
        model="qwen-max",
        api_key=api_key,
        streaming=True  # ✅ 明确声明支持流式
    )

def stream_chat(prompt: str):
    model = create_model()

    try:
        for chunk in model.stream(prompt):
            if chunk:  # ✅ 防止空chunk
                print(chunk, end="", flush=True)
    except Exception as e:
        print(f"\n❌ 调用失败: {e}")

if __name__ == "__main__":
    stream_chat("你是谁？请用一句话回答")