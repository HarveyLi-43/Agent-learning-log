from openai import OpenAI
import os

# 1.获取client对象 ---> 即创建OpenAI类对象
client = OpenAI(
    api_key=os.environ.get("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

# 2.调用模型
response = client.chat.completions.create(
    model="qwen3-max",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "磁通量公式"}

    ]
)

# 3.处理结果
print(response.choices[0].message.content)
