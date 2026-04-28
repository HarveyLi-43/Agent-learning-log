# =============================langcahin调用阿里云嵌入模型=======================================
from langchain_community.embeddings import DashScopeEmbeddings

# 初始化模型(创建模型对象) 不传model默认使用 text-embedding-v1
model = DashScopeEmbeddings()

# 不用invoke stream
# 用embed_query  embed_documents
print(model.embed_query("你好"))
print(model.embed_documents(["你好", "世界"]))


# =============================langcahin调用ollama的本地嵌入模型=================================
from langchain_community.embeddings import OllamaEmbeddings

model = OllamaEmbeddings(model="qwen-embedding:4b")

# 不用invoke stream
# 用embed_query  embed_documents
print(model.embed_query("你好"))
print(model.embed_documents(["你好", "世界"]))