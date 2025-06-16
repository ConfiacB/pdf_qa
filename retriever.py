from openai import OpenAI
import numpy as np

def embed_texts(texts, api_key):
    client = OpenAI(api_key=api_key)
    response = client.embeddings.create(
        input=texts,
        model="text-embedding-ada-002"
    )
    return [r.embedding for r in response.data]

def cosine_similarity(a, b):
    a, b = np.array(a), np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def retrieve_top_k(query, chunks, embeddings, api_key, k=3):
    query_embedding = embed_texts([query], api_key)[0]
    sims = [cosine_similarity(query_embedding, e) for e in embeddings]
    top_k_idx = sorted(range(len(sims)), key=lambda i: sims[i], reverse=True)[:k]
    return [chunks[i] for i in top_k_idx]
