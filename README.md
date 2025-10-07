# 📚 Simple RAG System with LangChain and Ollama

This repository contains a basic Retrieval-Augmented Generation (RAG) system built using LangChain, ChromaDB, and Ollama. The goal is to demonstrate how to use a Large Language Model (LLM) to answer questions based on a custom knowledge base (PDF documents) running entirely locally.

## ✨ Features

*   **Custom Knowledge Base:** Load your own PDF documents to create a domain-specific knowledge base.
*   **Local LLM and Embeddings:** Utilizes [Ollama](https://ollama.com/) to run both the embedding model (`nomic-embed-text`) and the Large Language Model (`mistral`) locally on your machine, ensuring data privacy and reducing API costs.
*   **Vector Database:** Employs [ChromaDB](https://www.trychroma.com/) as a lightweight, local vector store to efficiently search and retrieve relevant document chunks.
*   **Modular Design:** Separated concerns for embedding function, database population, and querying.
*   **Makefile for Convenience:** Simple commands to set up the database and run the query agent.

## 🚀 Getting Started

Follow these steps to get your RAG system up and running.

### Prerequisites

Before you begin, ensure you have the following installed:

1.  **Python 3.8+:**
    ```bash
    python3 --version
    ```
2.  **`pip` (Python package installer):**
    ```bash
    pip --version
    ```
3.  **Ollama:** Download and install Ollama from [ollama.com](https://ollama.com/).
    *   Once installed, start the Ollama server in a dedicated terminal:
        ```bash
        ollama serve
        ```
    *   Pull the necessary models:
        ```bash
        ollama pull nomic-embed-text
        ollama pull mistral
        ```

### Installation

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/callmemehdy/rag_system.git
    cd rag_system
    ```
    *(Note: Assuming your repo name is `rag_system` and username `callmemehdy`)*

2.  **Create a Virtual Environment (Recommended):**
    ```bash
    python3 -m venv v_env
    source v_env/bin/activate  # On Windows, use `v_env\Scripts\activate`
    ```

3.  **Install Python Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Prepare Your Data

1.  Create a folder named `data` in the root of your project directory:
    ```bash
    mkdir data
    ```
2.  Place your PDF documents (`.pdf` files) that you want to query into this `data` folder. For example:
    ```
    callmemehdy-rag_system/
    ├── data/
    │   ├── my_document_1.pdf
    │   └── my_document_2.pdf
    └── ...
    ```

### Populate the Database

This step processes your PDF documents, splits them into manageable chunks, creates numerical embeddings for these chunks using `nomic-embed-text`, and stores them in a local ChromaDB instance.

*   **Using `Makefile` (Recommended):**
    ```bash
    make setup_db
    ```
    This will create a `chroma` directory in your project containing the vector database.

*   **Manually:**
    ```bash
    python3 pop_db.py
    ```

*   **To reset and rebuild the database:**
    ```bash
    make reset_db
    # or manually:
    python3 pop_db.py --reset
    ```

## 💬 Querying the System

Once the database is populated, you can start asking questions! The system will retrieve relevant information from your PDFs and use the `mistral` LLM to formulate an answer.

*   **Using `Makefile` (Recommended):**
    ```bash
    make all
    ```
    This will first ensure the database is set up, then start the interactive query agent.

*   **Manually:**
    ```bash
    python3 evaluate_queries.py
    ```

The agent will prompt you with `query:`. Type your question and press Enter. To exit, type `EXIT`.

## Example Interaction

**In case you feed the agent the MariaDB documentation PDF:**

```text
agent loading...
query: which port the mariadb service runs on?
you will get your response after a while...
Response: port 3306.
query: EXIT
Bye!
```
