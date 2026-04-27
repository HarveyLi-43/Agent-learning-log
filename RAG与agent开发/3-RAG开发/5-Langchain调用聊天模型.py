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
    SystemMessage(content="你是一位语文老师"),
    HumanMessage(content="你会什么?"),
    AIMessage(content="我会写诗"),
    HumanMessage(content="写一首五言诗")
]

# 流式输出
for chunk in chat.stream(messages):
    if chunk.content:
        print(chunk.content, end="", flush=True)




# 真流式输出
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.callbacks import StreamingStdOutCallbackHandler
import os

chat = ChatTongyi(
    model="qwen3-max",
    api_key=os.environ.get("DASHSCOPE_API_KEY"),
    streaming=True,
    callbacks=[StreamingStdOutCallbackHandler()]
)

messages = [
    SystemMessage(content="你是一位语文老师"),
    HumanMessage(content="你会什么?"),
    AIMessage(content="我会写诗"),
    HumanMessage(content="写一首五言诗")
]

chat.invoke(messages)