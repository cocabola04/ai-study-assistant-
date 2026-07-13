# 📚 AI Study Assistant

An AI-powered Study Assistant built with **Python**, **Streamlit**, **ChromaDB**, and **Groq LLMs** that allows students to upload study material and ask questions in natural language. The application uses **Retrieval-Augmented Generation (RAG)** to retrieve relevant information from uploaded documents before generating answers, making responses accurate and context-aware.

---

## 🚀 Features

- 📄 Upload PDF study materials
- ✂️ Intelligent document chunking
- 🧠 Generate vector embeddings
- 🔍 Semantic search using ChromaDB
- 🤖 AI-powered question answering with Groq LLMs
- ⚡ Fast and interactive Streamlit interface
- 📚 Answers grounded in your uploaded notes

---

## 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Frontend | Streamlit |
| Backend | Python |
| LLM | Groq API |
| Embeddings | Sentence Transformers |
| Vector Database | ChromaDB |
| Document Processing | PyPDF |
| Environment | Python Dotenv |

---

## 📂 Project Structure

```text
ai-study-assistant/
│
├── .venv/                  # Virtual Environment
├── data/                   # Uploaded study material
├── database/               # Chroma database storage
├── datapdfs/               # PDF files
│
├── utils/
│   ├── __init__.py
│   ├── chunking.py         # Splits documents into chunks
│   ├── embeddings.py       # Embedding model
│   ├── pdf_reader.py       # Reads PDF documents
│   ├── rag.py              # RAG pipeline
│   ├── vector_store.py     # ChromaDB operations
│   └── database/           # Database utilities
│
├── .env                    # API keys
├── app.py                  # Streamlit application
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/ai-study-assistant.git
cd ai-study-assistant
```

---

### 2. Create a virtual environment

Windows

```bash
python -m venv .venv
```

Activate

```bash
.venv\Scripts\activate
```

macOS/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Create a `.env` file

```env
GROQ_API_KEY=your_api_key_here
```

---

### 5. Run the application

```bash
streamlit run app.py
```

---

## 🧠 How It Works

1. Upload one or more PDF documents.
2. Extract text from the PDFs.
3. Split the text into smaller chunks.
4. Convert each chunk into vector embeddings.
5. Store the embeddings in ChromaDB.
6. When a question is asked:
   - Retrieve the most relevant chunks using semantic similarity.
   - Send the retrieved context and question to the Groq LLM.
   - Display an accurate, context-aware response.

---

## 📸 Screenshots

Add screenshots of your application here.

Example:

```markdown
![Home Page](images/home.png)

![Answer Generation](images/answer.png)
```

---

## 📈 Future Improvements

- Support DOCX and TXT files
- Chat history
- Multiple document collections
- User authentication
- Source citations
- Streaming responses
- Hybrid search (BM25 + Vector Search)
- Conversation memory
- Multiple LLM providers (OpenAI, Gemini, Ollama)

---

## 📚 Concepts Demonstrated

- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Vector Embeddings
- ChromaDB
- Prompt Engineering
- Large Language Models
- Document Processing
- Streamlit Web Applications

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repository, open an issue, or submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.