## Langchain ecosystem
This is the repo that showcases the capabilities of Langchanin community. My main goal is to explore the capabilities of Langchain ecosystem and getting hands-on experience on various functionalities.

## Tech Stack:
- Python
- LangChain
- LangSMith - for LLM tracking purpose
- Streamlit


## Concepts explored:
- Open AI: 
    - How to invoke openAI API?
    - Simple application that reads a webpage and answers users query using OpenAI
- Ollama:
- Data Ingestion: Data loading techniques
- Data Transformer: Different data splitting techniques
- Embeddings: Different embedding techniques using OpenAI, Ollama, Huggingface
- Vector Stores: Different types of vector stores like FAISS, ChromaDB


## Prerequisites
- Setup Open AI account and load some money from https://platform.openai.com/
- Setup Langchain account and create API key from https://www.langchain.com/
- Setup Hugginface account and create access key from https://huggingface.co/
- Download and install Ollama from https://ollama.com/

### Some Commands used
- Create Python Virtual Environment
    ```sh
    python3 -m venv venv
    ```
- To activate Virtual Environment
    ```sh
    .\venv\Scripts\activate
    ```
- To run streamlit application
    ```sh
    streamlit run app.py --server.port 8502
    ```