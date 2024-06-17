import os

from dotenv import load_dotenv
from langchain.chains.llm import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEndpoint
from qdrant_client import QdrantClient

load_dotenv(dotenv_path="../../../dev.env")

repo_id = "mistralai/Mistral-7B-Instruct-v0.3"

prompt_template = """SYSTEM: You are an intelligent Yoga assistant helping the users with their questions on Yoga.

Question: {question}

Strictly Use ONLY the following pieces of context to answer the question at the end. Think step-by-step and then answer.
Context contain reference and metadata as well. Use that improve your answer quality.
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


def get_similar_content(input_query: str = None):
    client = QdrantClient(
        url=os.getenv("QDRANT_HOST"),
        api_key=os.getenv("QDRANT_API_KEY"),
        grpc_port=6334,
        prefer_grpc=True
    )
    search_result = client.query(
        collection_name=os.getenv('QDRANT_COLLECTION'),
        query_text=input_query,
        limit=10
    )
    client.close()
    return search_result


def generate_answer(query: str = None):
    llm = HuggingFaceEndpoint(
        repo_id=repo_id,
        max_length=512,
        temperature=0.25,
        huggingfacehub_api_token=os.getenv('HUGGINGFACEHUB_API_TOKEN'),
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    answer = chain({"context": get_similar_content(query), "question": query})
    # Print the summary
    print("Question:", answer['question'])
    print("Answer:", answer['text'])


generate_answer(query="Explain Yogic Counselling?")
generate_answer(query="List me 5 asanas which is beneficial for lung related issues?")
