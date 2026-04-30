from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_groq import ChatGroq
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import os

load_dotenv()

# Load PDF
loader = PyPDFLoader("Artificial_intelligence.pdf")
docs = loader.load()
print(f"Total pages loaded: {len(docs)}")

# Chunk it
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
chunks = splitter.split_documents(docs)
print(f"Total chunks created: {len(chunks)}")

# Create embeddings and save FAISS index
print("Creating embeddings... (this takes 1-2 minutes)")
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
vectorstore = FAISS.from_documents(chunks, embeddings)
vectorstore.save_local("faiss_index")
print("✅ FAISS index saved successfully!")