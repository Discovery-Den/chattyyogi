import os
import traceback

import streamlit as st
from dotenv import load_dotenv
from qdrant_client import QdrantClient

from embedding.prepare_response import generate_answer, message_func

st.set_page_config(
    page_title="Chatty Yogi",
    page_icon="🧘",
    layout="centered",
    initial_sidebar_state="auto",
)

st.title("🧘 Chatty Yogi 🧘🏻‍♂️")
st.caption("Talk to Chatty Yogi and know all about YNTC Course.")

st.session_state.history = []

load_dotenv(dotenv_path="../../dev.env")


def get_similar_content(input_query: str = None):
    try:
        client = QdrantClient(host=os.getenv("QDRANT_HOST"),
                              port=6333,
                              api_key=os.getenv("QDRANT_API_KEY"), )
        search_result = client.query(
            collection_name=os.getenv('QDRANT_COLLECTION'),
            query_text=input_query,
            limit=10
        )
        client.close()
        return search_result
    except Exception as e:
        st.error(f"Failed to connect to Qdrant: {e}")
        st.error(traceback.format_exc())
        return None


question = st.text_input("Ask Chatty Yogi a question:")

if question:
    context = get_similar_content(question)
    answer = generate_answer(context, question)
    st.session_state.history.append({"question": answer['question'], "answer": answer['text']})

# Display chat history
for i, entry in enumerate(st.session_state.history):
    is_user = i % 2 == 0
    message_func(entry['question'], is_user=False)
    message_func(entry['answer'], is_user=True)
