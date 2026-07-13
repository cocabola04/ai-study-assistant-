import streamlit as st
import os
from utils.pdf_reader import extract_text_from_pdf
from utils.chunking import split_text_into_chunks
from utils.embeddings import get_embeddings
from utils.vector_store import save_to_vector_store
from utils.rag import generate_answer, retrieve_context

# 1. Page Configuration
st.set_page_config(page_title="AI Study Assistant", layout="wide")

# 2. Sidebar for File Upload
with st.sidebar:
    st.header("Upload Notes")
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    
    if uploaded_file is not None:
        # Save the uploaded file temporarily to process it
        # We save it to data/pdfs/ so our pdf_reader can find it
        file_path = f"data/pdfs/{uploaded_file.name}"
        
        # Create a button to trigger processing
        if st.button("Process PDF"):
            with st.spinner("Reading, Chunking, and Indexing..."):
                # 1. Save file
                with open(file_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                
                # 2. Extract Text
                text = extract_text_from_pdf(file_path)
                
                # 3. Chunk Text
                chunks = split_text_into_chunks(text)
                
                # 4. Generate Embeddings & Save to DB
                # Note: This might take a few seconds
                save_to_vector_store(chunks)
                
                st.success(f"Processed {len(chunks)} chunks from {uploaded_file.name}!")
                st.info("You can now ask questions in the main chat.")

# 3. Main Chat Interface
st.header("AI Study Assistant Chat")

# Initialize chat history in session state if not exists
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. Chat Input
if prompt := st.chat_input("Ask a question about your notes"):
    # Display user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            # 1. Retrieve Context
            context = retrieve_context(prompt)
            
            # 2. Generate Answer
            response = generate_answer(prompt, context)
            
        st.markdown(response)
    
    # Add assistant response to history
    st.session_state.messages.append({"role": "assistant", "content": response})
