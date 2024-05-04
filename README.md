****NextGen SOP Management****

****Overview****

This is a chat search application that allows users to search for Standard Operating Procedures (SOPs) based on natural language queries. The application uses LangChain and Google Generative AI to retrieve relevant SOPs from a database.

****Requirements****
 
1.Python 3.8 or later
2.LangChain
3.LangChain Community
4.Hugging Face Transformers
5.FAISS (CPU or GPU)
6.Google Generative AI (requires API key)
7.Dotenv

****Installation****

Install the required libraries using pip: pip install -r requirements.txt
Create a .env file with your Google API key: GOOGLE_API_KEY=<>
Run the application using python (link unavailable)

****Usage****

The application will prompt the user to search for SOPs.
Enter a natural language query, and the application will retrieve relevant SOPs.
The results will be displayed in a list, with each result including the SOP title, description, and steps.

****Code Overview****
create_vector_db() creates a vector database from the SOP data in SOP.csv(This is KB which you can maintain ).
get_qa_chain() creates a QA chain using the vector database and Google Generative AI.
chat_search() runs the chat search application using the QA chain.
The application uses LangChain and Hugging Face Instruct Embeddings for text embedding and retrieval.
FAISS is used for efficient vector storage and retrieval.
Google Generative AI is used for generating answers based on the retrieved SOPs.

****Note****

This application requires a Google API key for the Google Generative AI library.
The langchain_google_genai library is not publicly available, and you may need to install it from a private repository or build it from source.
The application uses a simple prompt template for generating answers, and you may need to modify it to suit your specific use case.

  ![output-onlinegiftools (1)](https://github.com/rahulmakwana32/NextGenSop/assets/42233989/40be0983-e9b0-4eb9-8528-ba6dd5a5429f)
