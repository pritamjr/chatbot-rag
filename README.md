

# LLM-based RAG Chatbot

## Overview

This project implements a Retrieval-Augmented Generation (RAG) chatbot using an LLM (Large Language Model). The chatbot is designed to provide responses based on both user input and context retrieved from a vector database. It leverages the SentenceTransformer for generating embeddings and Faiss for efficient similarity search. The application is deployed using Streamlit for easy interaction.

## Features

- **Text Retrieval**: Uses Faiss for similarity search to retrieve relevant context from a pre-built vector index.
- **Response Generation**: Utilizes an LLM (Ollama's Llama3) to generate responses based on the retrieved context and user query.
- **User Interface**: Built with Streamlit to provide an interactive web interface for users to enter prompts and view responses.

## Requirements

- Python 3.8 or higher
- `sentence-transformers` library
- `faiss-cpu` library
- `streamlit` library
- `huggingface-hub` library
- `langchain_community` library

## Installation

1. Clone the repository:
   
    git clone https://github.com/your-repo/llm-rag-chatbot.git
    cd llm-rag-chatbot
  

2. Create and activate a virtual environment:
    
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
  

3. Install the required packages:
    
    pip install -r requirements.txt
    

4. Ensure you have your Faiss index file (`faiss_index.bin`) and texts file (`texts.json`) available in the `vector_db/` directory.



## Usage

1. Start the Streamlit server:
    
    streamlit run app.py
  

2. Open your web browser and navigate to `http://localhost:8501` to interact with the chatbot.

## Troubleshooting

- **Performance Issues**: If the chatbot is slow, ensure that the Faiss index is properly built and optimized.
- **Errors**: Check the console logs for detailed error messages and ensure all dependencies are correctly installed.

