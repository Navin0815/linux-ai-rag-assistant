"""
Vector Store Module
Creates and manages the Chroma vector database.
"""

from langchain_chroma import Chroma


class VectorStore:

    def __init__(self, embedding_model):
        self.embedding_model = embedding_model

    def create(self, documents):

        vector_db = Chroma.from_documents(
            documents=documents,
            embedding=self.embedding_model,
            persist_directory="db"
        )

        return vector_db