"""
Retriever Module
Performs semantic similarity search.
"""


class Retriever:

    def __init__(self, vector_db):
        self.vector_db = vector_db

    def search(self, query, k=3):

        results = self.vector_db.similarity_search(
            query,
            k=k
        )

        return results