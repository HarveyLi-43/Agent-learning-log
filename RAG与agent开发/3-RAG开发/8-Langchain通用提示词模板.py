from langchain_core.prompts import PromptTemplate
from langchain_community.llms.tongyi import Tongyi

# zero_shot
prompt_template = PromptTemplate.from_template(
    "你是一个{role}，请用{language}语言回复：{question}"
)

# # 调用 .format方法注入信息即可
# prompt_text = prompt_template.format(role="助手", language="中文", question="你是谁")
# model = Tongyi(model="qwen-max")
# response = model.invoke(input=prompt_text)
# print(response)

model = Tongyi(model="qwen-max")
chain = prompt_template | model
response = chain.invoke(input={"role": "助手", "language": "中文", "question": "你是谁"})
print(response)