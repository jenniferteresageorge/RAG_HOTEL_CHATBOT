import faiss
import numpy as np
import os
from sentence_transformers import SentenceTransformer
from .config import VECTOR_DB_PATH

model = SentenceTransformer("all-MiniLM-L6-v2")

def create_faiss_index(text_data):
    vectors = model.encode(text_data)
    d = vectors.shape[1]
    index = faiss.IndexFlatL2(d)
    index.add(np.array(vectors))
    
    # Save the FAISS index
    faiss.write_index(index, VECTOR_DB_PATH)
    return index

def load_faiss_index():
    if os.path.exists(VECTOR_DB_PATH):
        return faiss.read_index(VECTOR_DB_PATH)
    return None

def query_faiss(index, query_text, text_data, top_k=3):
    # Encode the query into a dense vector
    query_vector = model.encode([query_text], normalize_embeddings=True)

    # Convert to numpy and ensure float32 format for FAISS
    query_vector = np.array(query_vector).astype('float32')

    # Search for the top_k similar documents
    distances, idxs = index.search(query_vector, top_k)

    # Return the top matching documents
    return [text_data[i] for i in idxs[0] if i < len(text_data)]

