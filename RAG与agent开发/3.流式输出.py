from openai import OpenAI
import os

# 1.获取client对象 ---> 即创建OpenAI类对象
client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

# 2.调用模型
response = client.chat.completions.create(
    model="qwen3-max",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "你好"}
    ],
    stream=True
)

# 3.处理结果
for chunk in response:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)

