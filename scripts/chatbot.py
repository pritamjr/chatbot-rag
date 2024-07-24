import faiss
from sentence_transformers import SentenceTransformer
from langchain_community.llms import Ollama
import os


model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
llm = Ollama(model="llama3")


def load_texts():
    texts = []
    file_paths = [
        'data_extracted/pdf_text.txt',
        'data_extracted/website_text.txt',
        'data_extracted/youtube_transcript.txt'
    ]
    for path in file_paths:
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as file:
                texts.append(file.read())
        else:
            texts.append("")  
    return texts


def load_faiss_index():
    return faiss.read_index("vector_db/faiss_index.bin")


def query_faiss_index(query, index, texts, top_k=3):
    query_embedding = model.encode([query])
    distances, indices = index.search(query_embedding, top_k)
    results = [texts[i] for i in indices[0] if i < len(texts)]
    return " ".join(results)


def generate_response(prompt, context):
    full_prompt = context + "\n\n" + prompt
    response = llm.stream(full_prompt)
    return response


faiss_index = load_faiss_index()
texts = load_texts()

