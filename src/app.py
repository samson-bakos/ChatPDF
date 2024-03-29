import streamlit as st
from langchain_openai import OpenAI
from functions import *

llm = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("ChatPDF: Interactive Document Conversational Interface")

uploaded_file = st.file_uploader("Upload a PDF document", type=["pdf"])
if uploaded_file is not None:
    text = extract_text_from_pdf(uploaded_file)
    st.text_area("Extracted Text", value=text, height=300)

    user_query = st.text_input("Enter your query:")
    if user_query:
        text_chunks = split_text_recursive(text, max_length=10000)
        answer = query_llm(text_chunks, user_query, llm)
        st.write(f"Answer: {answer}")
