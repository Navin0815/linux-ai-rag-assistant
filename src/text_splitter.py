"""
Text Splitter Module
Splits documents into smaller chunks for embedding.
"""

from langchain.text_splitter import RecursiveCharacterTextSplitter


class TextSplitter:

    def __init__(self,
                 chunk_size=500,
                 chunk_overlap=100):

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )

    def split_documents(self, documents):

        return self.splitter.split_documents(documents)