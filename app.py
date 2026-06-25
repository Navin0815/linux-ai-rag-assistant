from src.loader import DocumentLoader


def main():

    loader = DocumentLoader("documents")

    documents = loader.load_documents()

    print("\n")

    print("=" * 60)

    print(f"Loaded {len(documents)} pages")

    print("=" * 60)

    print("\n")

    print(documents[0].page_content[:1000])


if __name__ == "__main__":
    main()