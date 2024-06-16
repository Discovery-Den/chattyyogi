from qdrant_client import QdrantClient
from qdrant_client.http import models

import os

os.environ['QDRANT_HOST'] = "https://3c78a67b-1cdb-4b5a-9944-1e27ce171122.us-east4-0.gcp.cloud.qdrant.io"
os.environ['QDRANT_API_KEY'] = "xIGGbFa5TeFS2IfEKyYRB9PlZufyPj2rY5dvS4t18HVGZIYsVqzNlQ"
os.environ['QDRANT_COLLECTION'] = "yntc_material"
os.environ['PORT'] = '6334'


def create_collection():
    """
    Create Chatti Yogi Collection with hybrid configuration
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
