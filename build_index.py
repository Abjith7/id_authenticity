from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

with open("knowledge.txt") as f:
    text = f.read()

splitter = CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=20
)

chunks = splitter.split_text(text)

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = FAISS.from_texts(chunks, embeddings)

db.save_local("vector_db")

print("Vector DB created")