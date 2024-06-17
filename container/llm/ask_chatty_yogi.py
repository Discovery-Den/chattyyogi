import os
import traceback

import streamlit as st
from dotenv import load_dotenv
from qdrant_client import QdrantClient
from streamlit_chat import message

from embedding.prepare_response import generate_answer

st.title("🧘 Chatty Yogi 🧘🏻‍♂️")
st.caption("Talk to Chatty Yogi and know all about YNTC Course.")

question = st.text_input("Ask Chatty Yogi a question:")

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


if question:
    context = get_similar_content(question)
    answer = generate_answer(context, question)
    st.session_state.history.append({"question": answer['question'], "answer": answer['text']})

# Display chat history
for i, entry in enumerate(st.session_state.history):
    is_user = i % 2 == 0
    avatar_style = "user" if is_user else "chatbot"
    message(entry['question'], is_user=True, key=str(i) + '_user', avatar_style="open-peeps")
    message(entry['answer'], is_user=False, key=str(i) + '_bot', avatar_style="bottts")
