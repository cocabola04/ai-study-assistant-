import streamlit as st
import os
import uuid
from utils.pdf_reader import extract_text_from_pdf
from utils.chunking import split_text_into_chunks
from utils.embeddings import get_embeddings
from utils.vector_store import save_to_vector_store
from utils.rag import generate_answer, retrieve_context
from utils.session_manager import cleanup_old_sessions

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(page_title="AI Study Assistant", layout="wide")


cleanup_old_sessions()

# -------------------------------
# Create a unique session ID
# -------------------------------
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

# -------------------------------
# Sidebar for File Upload
# -------------------------------
with st.sidebar:
    st.header("Upload Notes")
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file is not None:

        file_path = f"data/pdfs/{uploaded_file.name}"

        if st.button("Process PDF"):

            with st.spinner("Reading, Chunking, and Indexing..."):

                # Create directory if needed
                os.makedirs("data/pdfs", exist_ok=True)

                # Save uploaded file
                with open(file_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())

                # Extract text
                text = extract_text_from_pdf(file_path)

                # Chunk text
                chunks = split_text_into_chunks(text)

                # Save to THIS USER'S vector database
                save_to_vector_store(
                    chunks,
                    session_id=st.session_state.session_id,
                )

                st.success(
                    f"Processed {len(chunks)} chunks from {uploaded_file.name}!"
                )

                st.info("You can now ask questions in the main chat.")

# -------------------------------
# Chat Interface
# -------------------------------
st.header("AI Study Assistant Chat")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -------------------------------
# Chat Input
# -------------------------------
if prompt := st.chat_input("Ask a question about your notes"):

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            context = retrieve_context(
                prompt,
                session_id=st.session_state.session_id,
            )

            response = generate_answer(
                prompt,
                context,
            )

        st.markdown(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response,
        }
    )