import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from config import KB_PATH, VECTOR_DB_PATH


def build_vector_store():

    documents = []

    # Load all text files from KB folder
    for file in os.listdir(KB_PATH):

        if file.endswith(".txt"):

            loader = TextLoader(os.path.join(KB_PATH, file))

            docs = loader.load()

            documents.extend(docs)

    if len(documents) == 0:
        raise ValueError("No documents loaded from KB folder")

    # Split documents
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    texts = text_splitter.split_documents(documents)

    # Create embeddings
    embeddings = HuggingFaceEmbeddings()

    # Create FAISS vector store
    vectorstore = FAISS.from_documents(texts, embeddings)

    return vectorstore

def load_vector_store():

    embeddings = HuggingFaceEmbeddings()

    # If vectorstore does not exist → build it
    if not os.path.exists(os.path.join(VECTOR_DB_PATH, "index.faiss")):

        print("Vector store not found. Building new vector store...")

        vectorstore = build_vector_store()

        vectorstore.save_local(VECTOR_DB_PATH)

        return vectorstore

    # Otherwise load existing one
    else:

        print("Loading existing vector store...")

        vectorstore = FAISS.load_local(
            VECTOR_DB_PATH,
            embeddings,
            allow_dangerous_deserialization=True
        )

        return vectorstore