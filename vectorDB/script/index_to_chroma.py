import json
import chromadb
from chromadb.utils import embedding_functions
from sentence_transformers import SentenceTransformer

# Load data
with open("/workspace/vectorDB/script/healthcare_docs.json", "r") as f:
    docs = json.load(f)

# Initialize Chroma and embedding model
chroma_client = chromadb.PersistentClient(path="/workspace/vectorDB/healthcare_db")
collection = chroma_client.get_or_create_collection(name="healthcare")

# Use SentenceTransformer for embeddings
embedder = SentenceTransformer("all-MiniLM-L6-v2")  # Lightweight, fast

# Prepare docs
texts = [doc["text"] for doc in docs]
ids = [doc["id"] for doc in docs]

# Add to Chroma
collection.add(
    documents=texts,
    ids=ids
)

print(f" Indexed {len(docs)} documents into ChromaDB!")
