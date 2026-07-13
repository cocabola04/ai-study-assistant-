def split_text_into_chunks(text, chunk_size=1000, chunk_overlap=200):
    """
    Splits a large text into smaller chunks with overlap.
    
    Args:
        text (str): The full text to split.
        chunk_size (int): The maximum size of each chunk (in characters).
        chunk_overlap (int): How many characters overlap between chunks.
        
    Returns:
        list: A list of text chunks.
    """
    
    # If text is shorter than chunk size, return it as is
    if len(text) <= chunk_size:
        return [text]
    
    chunks = []
    start = 0
    
    # Loop through the text
    while start < len(text):
        # Define the end of this chunk
        end = start + chunk_size
        
        # Extract the chunk
        chunk = text[start:end]
        chunks.append(chunk)
        
        # Move the start pointer forward
        # We subtract overlap so the next chunk starts inside the previous one
        start += chunk_size - chunk_overlap
        
        # Safety break: If the last chunk was very small, don't loop forever
        if start >= len(text):
            break
            
    return chunks

# Test block
if __name__ == "__main__":
    # A dummy long text to test
    long_text = """
    Artificial Intelligence (AI) is intelligence demonstrated by machines, 
    as opposed to the natural intelligence displayed by animals including humans. 
    AI research has been defined as the field of study of intelligent agents, 
    which refers to any system that perceives its environment and takes actions 
    that maximize its chance of achieving its goals. The term "artificial intelligence" 
    had previously been used to describe machines that mimic and "display" human mind/skills, 
    and/or emulate the human mind and imitate its behavior.
    """ * 10 # Repeat this text 10 times to make it long
    
    print(f"Total text length: {len(long_text)} characters")
    
    # Split it
    chunks = split_text_into_chunks(long_text, chunk_size=200, chunk_overlap=50)
    
    print(f"Number of chunks created: {len(chunks)}\n")
    
    # Print the first 3 chunks to see the overlap
    for i, chunk in enumerate(chunks[:3]):
        print(f"--- Chunk {i+1} ---")
        print(chunk)
        print("-" * 20)
