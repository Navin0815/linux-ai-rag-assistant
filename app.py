from src.loader import DocumentLoader
from src.text_splitter import TextSplitter


def main():

    loader = DocumentLoader("documents")
    documents = loader.load_documents()

    splitter = TextSplitter()

    chunks = splitter.split_documents(documents)

    print("=" * 60)
    print(f"Pages Loaded : {len(documents)}")
    print(f"Chunks Created : {len(chunks)}")
    print("=" * 60)

    print(chunks[0].page_content)


if __name__ == "__main__":
    main()