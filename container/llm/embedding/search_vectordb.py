import os
import streamlit as st
from dotenv import load_dotenv
from qdrant_client import QdrantClient
import traceback

load_dotenv(dotenv_path="../../../dev.env")



