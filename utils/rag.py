import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq
from utils.vector_store import query_vector_store

# 1. Load Environment Variables
load_dotenv()

# 2. Configure Groq
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    # Check Streamlit Cloud Secrets
    api_key = st.secrets.get("GROQ_API_KEY")

if not api_key:
    # Fallback: Check if they put it in GOOGLE_API_KEY by mistake
    api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError(
        "GROQ_API_KEY not found. Please add it to your .env file or Streamlit Secrets."
    )

client = Groq(api_key=api_key)


def retrieve_context(question, session_id, n_results=3):
    """
    Takes a user question, searches the user's own database,
    and returns the relevant text snippets.
    """
    print(f"Searching database for: '{question}'...")

    results = query_vector_store(
        question,
        session_id=session_id,
        n_results=n_results,
    )

    if not results:
        return "No relevant information found in the database."

    context = "\n\n".join(results)
    return context


def generate_answer(question, context):
    """
    Sends the question and context to Groq to get an answer.
    """

    prompt = f"""
    You are a helpful study assistant.

    Answer the question based ONLY on the context provided below.

    If the context does not contain the answer, say:
    "I don't know based on the provided notes."

    Context:
    {context}

    Question:
    {question}

    Answer:
    """

    print("Asking Groq for an answer...")

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama-3.1-8b-instant",
    )

    response = chat_completion.choices[0].message.content

    return response


# Test block
if __name__ == "__main__":
    user_question = "How does a plant create food?"

    session = "test_session"

    retrieved_text = retrieve_context(
        user_question,
        session_id=session,
    )

    final_answer = generate_answer(
        user_question,
        retrieved_text,
    )

    print("Answer:", final_answer)