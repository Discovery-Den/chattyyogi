from qdrant_client import QdrantClient
from qdrant_client.http import models
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="../../../dev.env")


def create_collection():
    """
    Create Chatty Yogi Collection with hybrid configuration
    :return: custom collection with hybrid collection
    """

    client = QdrantClient(
        url=os.getenv("QDRANT_HOST"),
        api_key=os.getenv("QDRANT_API_KEY"),
        grpc_port=6334,
        prefer_grpc=True
    )
    client.create_collection(
        collection_name=os.getenv("QDRANT_COLLECTION"),
        vectors_config={
            "fast-bge-small-en": models.VectorParams(
                size=384,  # fastembed
                distance=models.Distance.COSINE,
            )
        },
        sparse_vectors_config={
            "text-sparse": models.SparseVectorParams(
                index=models.SparseIndexParams(
                    on_disk=True,
                )
            )
        },
    )
    client.close()


create_collection()
