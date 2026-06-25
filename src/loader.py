"""
Document Loader Module
----------------------
Loads PDF documents from the documents folder.
"""

from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader


class DocumentLoader:
    """
    Loads PDF documents.
    """

    def __init__(self, documents_path: str):

        self.documents_path = Path(documents_path)

    def load_documents(self):

        documents = []

        pdf_files = sorted(self.documents_path.glob("*.pdf"))

        if not pdf_files:
            raise FileNotFoundError(
                f"No PDF files found in {self.documents_path}"
            )

        for pdf in pdf_files:

            print(f"Loading {pdf.name}")

            loader = PyPDFLoader(str(pdf))

            documents.extend(loader.load())

        return documents