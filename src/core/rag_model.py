#from transformers import pipeline
from .vector_store import create_faiss_index, load_faiss_index, query_faiss
from .data_loader import load_data
#from .config import LLM_MODEL_NAME
import cohere
import os
from dotenv import load_dotenv
load_dotenv()

cohere_api_key = os.getenv("COHERE_API_KEY")
co = cohere.Client(cohere_api_key)

df = load_data()
text_data = df[['hotel', 'country', 'reservation_status']].astype(str).agg(' '.join, axis=1).tolist()

index = load_faiss_index()
if index is None:
    index = create_faiss_index(text_data)

def ask_question(query):
    retrieved_docs = query_faiss(index, query, text_data, top_k=3)
    context = "\n".join(dict.fromkeys(retrieved_docs))  # remove duplicates

    system_prompt = (
        "You are a helpful and friendly hotel booking assistant. Answer the user's question in a polite, detailed, and informative manner using the provided context."
    )
    full_prompt = f"{system_prompt}\n\nContext:\n{context}\n\nQuestion:\n{query}\n\nAnswer:"

    response = co.generate(
        prompt=full_prompt,
        model="command-r-plus",
        max_tokens=300,
        temperature=0.4,
        stop_sequences=["Question:", "Context:"]
    )

    return response.generations[0].text.strip()

