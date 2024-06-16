from langchain.chains.llm import LLMChain
from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain_community.embeddings import FastEmbedEmbeddings
from langchain_huggingface import HuggingFaceEndpoint
from langchain_community.llms.huggingface_endpoint import HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from qdrant_client import QdrantClient
import os

from qdrant_client.http.models import models

os.environ['QDRANT_HOST'] = "https://3c78a67b-1cdb-4b5a-9944-1e27ce171122.us-east4-0.gcp.cloud.qdrant.io"
os.environ['QDRANT_API_KEY'] = ""
os.environ['QDRANT_COLLECTION'] = "yntc_material"
os.environ['PORT'] = '6334'

client = QdrantClient(
    url=os.getenv("QDRANT_HOST"),
    api_key=os.getenv("QDRANT_API_KEY"),
    grpc_port=6334,
    prefer_grpc=True
)

# retrieve = cli
# embeddings = FastEmbedEmbeddings()
# qdrant = Qdrant(client, os.getenv('QDRANT_COLLECTION'), vector_name="fast-bge-small-en")
# retriever = qdrant.as_retriever(search_type="mmr",
#                                 search_kwargs={'k': 6, 'lambda_mult': 0.25})
# search_result = retriever.invoke("List of yoga asana for lung related issue")
# search_result = qdrant.similarity_search("List of yoga asana for lung related issue")

search_result =client.query(
    collection_name=os.getenv('QDRANT_COLLECTION'),
    query_text="List of yoga asana for lung related issue",
    limit=10
)

client.close()

print(search_result)

question = "What is Experimentation?"
prompt_template = """SYSTEM: You are an intelligent Yoga assistant helping the users with their questions on Yoga.

Question: {question}

Strictly Use ONLY the following pieces of context to answer the question at the end. Think step-by-step and then answer.

Do not try to make up an answer: - If the answer to the question cannot be determined from the context alone, 
say "I cannot determine the answer to that." - If the context is empty, just say "I do not know the answer to that."

=============
{context}
=============

Question: {question}
Helpful Answer:"""

prompt = PromptTemplate(
    template=prompt_template, input_variables=["context", "question"]
)

repo_id = "meta-llama/Meta-Llama-3-8B"
os.environ['HF_API_KEY'] = ''

llm = HuggingFaceEndpoint(
    repo_id=repo_id,
    temperature=0.5,
    huggingfacehub_api_token=os.getenv('HF_API_KEY'),
)

chain = LLMChain(llm=llm, prompt=prompt)
summary = chain.run(search_result, "List of yoga asana for lung related issue")

# Print the summary
print("Summary:")
print(summary)