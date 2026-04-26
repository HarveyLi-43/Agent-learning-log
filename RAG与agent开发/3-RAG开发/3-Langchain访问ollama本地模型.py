# langchain_ollama
from langchain_ollama import OllamaLLM

model = OllamaLLM(model="deepseek-r1:1.5b")

# 用invoke访问模型
response = model.invoke("你好")

print(response)