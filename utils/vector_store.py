import chromadb
from utils.embeddings import get_embeddings
from utils.session_manager import register_session

# Create ChromaDB client
client = chromadb.PersistentClient(path="database")


def get_collection(session_id):
    """
    Returns a unique collection for each user session.
    """
    return client.get_or_create_collection(
        name=f"study_notes_{session_id}"
    )


def save_to_vector_store(chunks, session_id, metadata_list=None):
    """
    Saves document chunks into the session-specific Chroma collection.
    """

    collection = get_collection(session_id)
    
    register_session(collection.name)
    

    # Clear previous uploads for THIS SESSION ONLY
    existing = collection.get()

    if existing["ids"]:
        collection.delete(ids=existing["ids"])

    # Generate IDs
    ids = [str(i) for i in range(len(chunks))]

    print("Generating embeddings...")

    embeddings = get_embeddings(chunks)

    collection.add(
        documents=chunks,
        embeddings=embeddings,
        ids=ids,
        metadatas=metadata_list if metadata_list else [None] * len(chunks),
    )

    print(f"Successfully saved {len(chunks)} chunks to the database.")


def query_vector_store(query_text, session_id, n_results=3):
    """
    Searches ONLY the current user's collection.
    """

    collection = get_collection(session_id)

    query_embedding = get_embeddings(query_text)

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=n_results,
    )

    if len(results["documents"]) == 0:
        return []

    return results["documents"][0]


# TEST BLOCK
if __name__ == "__main__":

    session = "test_session"

    sample_notes = [
        "Photosynthesis is the process by which plants use sunlight to create food.",
        "The mitochondria is the powerhouse of the cell.",
        "Python is a high-level programming language.",
    ]

    save_to_vector_store(sample_notes, session)

    print(query_vector_store("energy", session))