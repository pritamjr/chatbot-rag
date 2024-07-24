import streamlit as st
from scripts.chatbot import query_faiss_index, generate_response, faiss_index, texts

st.title("Chat with LLM-based RAG Chatbot")

prompt = st.text_area("Enter your prompt:")

if st.button("Generate"):
    if prompt:
        with st.spinner("Generating response..."):
            context = query_faiss_index(prompt, faiss_index, texts)
            response = generate_response(prompt, context)
            st.write(response)
