from sentence_transformers import SentenceTransformer

def get_embeddings(text_list):
    """
    Converts a list of text strings into a list of vector embeddings (numbers).
    
    Args:
        text_list (list): A list of strings (e.g., our chunks).
        
    Returns:
        list: A list of lists (the vectors).
    """
    
    print("loading AI model... ")
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(text_list)
    return embeddings

# test block
if __name__ == "__main__":

    # Sample sentences to test
    sentences = [
        "The cat sits on the mat.",
        "A dog is playing in the park.",
        "I love eating pizza for dinner.",
        "The feline is resting on the rug." # Similar to the first sentence
    ]
    
    print(f"Generating embeddings for {len(sentences)} sentences...")
    
    #get vectors here
    vectors = get_embeddings(sentences)
    
    print("\n ---Results---")
    
    # Show the shape of the first vector
    # This model creates vectors with 384 numbers (dimensions)
    print(f"Vector size (dimensions): {len(vectors[0])}")
    
    # Print the actual numbers for the first sentence
    print(f"\nFirst sentence: '{sentences[0]}'")
    print(f"First 10 numbers of its vector: {vectors[0][:10]}")
    
    # Print the numbers for the last sentence (similar meaning)
    print(f"\nLast sentence: '{sentences[3]}'")
    print(f"First 10 numbers of its vector: {vectors[3][:10]}")
    
    print("\nNotice how the numbers for 'cat' and 'feline' look somewhat similar compared to 'pizza'!")
