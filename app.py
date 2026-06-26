from src.loader import DocumentLoader
from src.text_splitter import TextSplitter
from src.embeddings import EmbeddingModel
from src.vector_store import VectorStore
from src.retriever import Retriever


def main():

    print("\nLoading documents...")

    loader = DocumentLoader("documents")
    docs = loader.load_documents()

    print(f"Loaded {len(docs)} pages")

    splitter = TextSplitter()
    chunks = splitter.split_documents(docs)

    print(f"Created {len(chunks)} chunks")

    embedding_model = EmbeddingModel().get_embedding_model()

    print("Creating embeddings...")

    vector_db = VectorStore(
        embedding_model
    ).create(chunks)

    print("\n✅ Vector Database Created Successfully!")
    print(f"Stored {len(chunks)} document chunks.")

    # ----------------------------
    # Semantic Search
    # ----------------------------

    query = "What is DevSecOps?"

    print("\nSearching...")

    results = Retriever(vector_db).search(query)

    print("=" * 60)

    for i, doc in enumerate(results, start=1):
        print(f"\nResult {i}\n")
        print(doc.page_content[:400])
        print("-" * 60)


if __name__ == "__main__":
    main()