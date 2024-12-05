# Using only local models, based on https://docs.llamaindex.ai/en/stable/examples/embeddings/huggingface/
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings

Settings.llm = Ollama(model="llama3.2", request_timeout=120.0)
Settings.emb2ed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5"
)

# Quering a folder with a bunch of docx and pptx files, based on https://docs.llamaindex.ai/en/stable/understanding/putting_it_all_together/q_and_a/#semantic-search
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
documents = SimpleDirectoryReader(input_dir="data").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()
response = query_engine.query("What are the most important topics raised?")
print(response)

