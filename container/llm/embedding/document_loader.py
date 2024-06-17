import os

from dotenv import load_dotenv
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from qdrant_client import QdrantClient

load_dotenv(dotenv_path="../../../dev.env")


def get_qdrant_client():
    return QdrantClient(
        url=os.getenv("QDRANT_HOST"),
        api_key=os.getenv("QDRANT_API_KEY"),
        grpc_port=6334,
        prefer_grpc=True
    )


def load_files(folder_path: str = "../resource/"):
    """
    Read all the pdf files from the folder and pass it for text transformation
    :param folder_path: path of resource files
    :return: List[Documents]
    """

    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(folder_path, filename)
            print("Reading pdf file: ", filename)
            loader = PyMuPDFLoader(file_path=pdf_path, extract_images=True)
            pages = loader.load_and_split()
            text_splitter(pages=pages)


def text_splitter(pages):
    """
    Split list of documents into list of text chunks. Document contain content and metadata
    :param pages: List[Documents]
    :return: List[Documents]
    """
    content_splitter = CharacterTextSplitter(
        separator="\n", chunk_size=1000, chunk_overlap=150, length_function=len
    )
    docs = content_splitter.split_documents(pages)
    print("Pages in the original document: ", len(pages))
    print("Length of chunks after splitting pages: ", len(docs))
    add_content(docs=docs)


def add_content(docs):
    """
    Add content along with metadata into qdrant collection
    :param docs:
    :return:
    """

    texts, metadata = [], []
    for doc in docs:
        texts.append(doc.page_content)
        metadata.append(doc.metadata)

    client = get_qdrant_client()
    # embeddings = FastEmbedEmbeddings()
    client.add(
        collection_name=os.getenv("QDRANT_COLLECTION"),
        documents=texts,
        metadata=metadata
    )

    client.close()


def load_all_text_book_in_collection():
    """
    Read all the yoga text books from the resource and add it into vector DB collection
    :return: None
    """

    load_files()


load_all_text_book_in_collection()
