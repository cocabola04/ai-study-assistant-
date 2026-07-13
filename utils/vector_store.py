import chromadb
from chromadb.config import Settings
from utils.embeddings import get_embeddings 

client = chromadb.PersistentClient(path = "database")

collection = client.get_or_create_collection(name="study_notes")

def save_to_vector_store(chunks, metadata_list = None):
    #ids for chunks eg - 0,1,2,3
    ids = [str(i) for i in range(len(chunks))]  
    
    #generate embeddings for the chunks 
    print("Generating embeddings... ")
    embeddings = get_embeddings(chunks) 
    
    
    #add to chromaDB
    collection.add(
        documents = chunks,
        embeddings = embeddings,
        ids = ids,
        metadatas = metadata_list if metadata_list else [None]*len(chunks)  
    )
    
    print(f"Successfully saved {len(chunks)} chunks to the database.")
    
def query_vector_store(query_text, n_results=3):
    """
    Searches the database for text similar to the query.
    
    Args:
        query_text (str): The question or search term.
        n_results (int): How many results to return.
        
    Returns:
        list: The matching text chunks.
    """
    #convert questions into vectors 
    query_embeddings = get_embeddings(query_text)
    
    
    #search ChromaDB
    results = collection.query(
        query_embeddings = query_embeddings,
        n_results = n_results
    )
    
    #returning the documents 
    return results['documents'][0]

#TEST BLOCK

if __name__ == "__main__":
    print("Debug: Starting vector store test...")
    
    # 1. Create some dummy data
    sample_notes = [
        "Photosynthesis is the process by which plants use sunlight to create food.",
        "The mitochondria is the powerhouse of the cell.",
        "Python is a high-level programming language popular for data science.",
        "JavaScript is commonly used for web development in the browser.",
        "Gravity is the force that attracts a body toward the center of the earth."
    ]
    
    #save to DB
    
    try:
        save_to_vector_store(sample_notes)   
    except Exception as e:
        print(f"Error (might be duplicates) : {e}")
        
    #search the DB
    print("\n --Searching for 'energy'--")
    results = query_vector_store("energy")
    for i, res in enumerate(results):
        print(f"results {i+1} :  {res}")    
        