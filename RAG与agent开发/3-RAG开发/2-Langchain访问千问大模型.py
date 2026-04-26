import os
# langchain_community
from langchain_community.llms.tongyi import Tongyi

model = Tongyi(model="qwen-max", api_key=os.environ.get("DASHSCOPE_API_KEY"))
# 不用qwen3- max,是因为qwen3-max是聊天模型，qwen-max是大语言模型

# 用invoke访问模型
response = model.invoke("你好")

print(response)