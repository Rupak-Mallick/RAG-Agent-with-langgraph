
# AI Agent Automation System with LangGraph(RAG Agent)

## Use Case
A customer support automation system where the AI agent handles incoming queries, retrieves relevant data, and generates accurate responses using Retrieval-Augmented Generation (RAG) and LangGraph.

## Features
- Query understanding and intent recognition
- Knowledge base retrieval with vector search
- LangGraph agent for automated, multi-step reasoning
- Response generation using LLM (e.g., Mistral, GPT-compatible)
- Modular and testable codebase

## Project Structure
- `RAG_assignment1.ipynb` — Main implementation notebook
- `tests/` — Unit tests and validation scripts
- `demo/` — Example queries to showcase system capabilities
- `README.md` — Documentation

## Setup Instructions
1. Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
2. Launch the notebook:
    ```bash
    jupyter notebook RAG_assignment1.ipynb
    ```

## Requirements
- Python 3.8+
- LangGraph
- LangChain
- FAISS / ChromaDB
- SentenceTransformers / HuggingFace Embeddings
- LLM API (e.g., Groq, OpenAI, or Ollama)

## Demo
Includes simulated customer queries with automatic responses based on embedded product documentation or FAQs.

## License
MIT License
