# NextGen SOP Management

## Overview

This  application  allows users to search for Standard Operating Procedures (SOPs) based on natural language queries. The application uses LangChain and Google Generative AI to retrieve relevant SOPs from a database.

## Requirements

- Python 3.8 or later
- LangChain
- LangChain Community
- Hugging Face Transformers
- FAISS (CPU or GPU)
- Google Generative AI (requires API key)
- Dotenv

## Installation

1. Install the required libraries using pip: `pip install -r requirements.txt`
2. Create a `.env` file with your Google API key: `GOOGLE_API_KEY=<your_api_key>`
3. Run the application using python.

## Usage

1. The application will prompt the user to search for SOPs.
2. Enter a natural language query, and the application will retrieve relevant SOPs.
3. The results will be displayed in a list, with each result including the SOP title, description, and steps.

## Code Overview

- `create_vector_db()`: Creates a vector database from the SOP data in `SOP.csv`.
- `get_qa_chain()`: Creates a QA chain using the vector database and Google Generative AI.
- `chat_search()`: Runs the chat search application using the QA chain.

The application uses LangChain and Hugging Face Instruct Embeddings for text embedding and retrieval. FAISS is used for efficient vector storage and retrieval. Google Generative AI is used for generating answers based on the retrieved SOPs.

## Note

- This application requires a Google API key for the Google Generative AI library.
- The `langchain_google_genai` library may not be publicly available and may need to be installed from a private repository or built from source.
- The application uses a simple prompt template for generating answers, and you may need to modify it to suit your specific use case.

## References
- https://instructor-embedding.github.io/
- https://www.youtube.com/watch?v=AjQPRomyd-k&t=1175s
  
## WorkFlow

  ![output-onlinegiftools (1)](https://github.com/rahulmakwana32/NextGenSop/assets/42233989/40be0983-e9b0-4eb9-8528-ba6dd5a5429f)
