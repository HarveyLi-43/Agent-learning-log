import os
from openai import OpenAI

client = OpenAI(
    api_key="",
    base_url="http://localhost:11434/v1") # 注意这里用的是openai的客户端，所以必须是 /v1

response = client.chat.completions.create(
    model="deepseek-r1:RAG与agent开发.5b",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "热力学几大定律"},
    ],
    stream=True
)

for chunk in response:
    print(chunk.choices[0].delta.content, end="", flush=True)