from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
import os

# 初始化模型
chat = ChatTongyi(
    model="qwen3-max",
    api_key=os.environ.get("DASHSCOPE_API_KEY"),
    stream=True
)

# 准备消息list
messages = [
    ("system", "你一位语文老师"),
    ("human", "你会什么?"),
    ("ai", "我会写诗"),
    ("human", "写一首五言诗")
]

# 流式输出
for chunk in chat.stream(messages):
    if chunk.content:
        print(chunk.content, end="", flush=True)





# 真流式输出(langchain更新后，上面的方式不能流式输出)
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.callbacks import StreamingStdOutCallbackHandler


chat = ChatTongyi(
    model="qwen3-max",
    streaming=True,
    callbacks=[StreamingStdOutCallbackHandler()]
)

messages = [
    ("system", "你一位语文老师"),
    ("human", "你会什么?"),
    ("ai", "我会写诗"),
    ("human", "写一首五言诗")
]

chat.invoke(messages)