import os
import streamlit as st
from app_tab1 import render_story_tab
from app_tab5 import render_personal_qa_tab
from vertexai.preview.generative_models import GenerativeModel
import vertexai
import logging
from google.cloud import logging as cloud_logging

# configure logging
logging.basicConfig(level=logging.INFO)
# attach a Cloud Logging handler to the root logger
log_client = cloud_logging.Client()
log_client.setup_logging()

PROJECT_ID = os.environ.get('PROJECT_ID')   # Your Qwiklabs Google Cloud Project ID
LOCATION = os.environ.get('REGION')         # Your Qwiklabs Google Cloud Project Region
vertexai.init(project=PROJECT_ID, location=LOCATION)

@st.cache_resource
def load_models():
    # Using a more powerful model with a larger context window is ideal for this RAG use case.
    text_model = GenerativeModel("gemini-2.5-pro")
    multimodal_model = GenerativeModel("gemini-2.5-pro")
    return text_model, multimodal_model

st.header("Derrick's Cloud Question App", divider="red")

text_model, multimodal_model = load_models()

tab1, tab5  = st.tabs([ "Derrick Kaliney Q&A","Story"])

with tab1:
    render_personal_qa_tab(text_model)

with tab5:
    render_story_tab(text_model)
