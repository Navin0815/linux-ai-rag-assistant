from src.embeddings import EmbeddingModel


def main():

    model = EmbeddingModel()

    embedding = model.get_embedding_model()

    vector = embedding.embed_query(
        "What is DevSecOps?"
    )

    print(f"Embedding Length : {len(vector)}")

    print(vector[:10])


if __name__ == "__main__":
    main()