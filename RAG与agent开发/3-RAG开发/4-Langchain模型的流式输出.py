# langchain_community
import os
from langchain_community.llms.tongyi import Tongyi

model = Tongyi(model="qwen-max", api_key=os.environ.get("DASHSCOPE_API_KEY"))

# 用stream访问模型
response = model.stream("你是谁?")
for chunk in response:
    print(chunk, end="", flush=True)



# langchain_ollama
from langchain_ollama import OllamaLLM

model = OllamaLLM(model="deepseek-r1:1.5b")

# 用stream访问模型
response = model.stream("你是谁？")
for chunk in response:
    print(chunk, end="", flush=True)