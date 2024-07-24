import faiss
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')  # This model does not have TensorFlow/Keras dependency

def create_faiss_index(text_data):
    embeddings = model.encode(text_data)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    return index

def load_texts():
    with open("data_extracted/pdf_text.txt") as f:
        pdf_text = f.read()
    with open("data_extracted/website_text.txt") as f:
        website_text = f.read()
    with open("data_extracted/youtube_transcript.txt") as f:
        youtube_transcript = f.read()
    return [pdf_text, website_text, youtube_transcript]

texts = load_texts()
faiss_index = create_faiss_index(texts)

# Save the index
faiss.write_index(faiss_index, "vector_db/faiss_index.bin")
