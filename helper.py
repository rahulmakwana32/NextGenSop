

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

from langchain.document_loaders.csv_loader import CSVLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceInstructEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA


from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI

load_dotenv()  # take environment variables from .env (especially openai api key)






#Function is Used to to load and embed SOP
# # Initialize instructor embeddings using the Hugging Face model
instructor_embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
vectordb_file_path = "faiss_index"
api_key = "AIzaSyBJXkeC8xkWlsDwLZserPIvN6w3CQcD0Ug"
llm = GoogleGenerativeAI(model="models/text-bison-001", google_api_key=api_key)


def create_vector_db():
    # Load data from FAQ sheet
    loader = CSVLoader(file_path='SOP.csv')
    data = loader.load()

    # Create a FAISS instance for vector database from 'data'
    vectordb = FAISS.from_documents(documents=data,
                                    embedding=instructor_embeddings)

    # Save vector database locally
    vectordb.save_local(vectordb_file_path)





def get_qa_chain():
    # Load the vector database from the local folder
    vectordb = FAISS.load_local(vectordb_file_path, instructor_embeddings, allow_dangerous_deserialization=True)

    # Create a retriever for querying the vector database
    retriever = vectordb.as_retriever(score_threshold=0.7)

    prompt_template = """Given the following context and a question, generate an answer based on this context only.
    In the answer try to provide as much text as possible from "response" section in the source document context without making much changes.
    If the answer is not found in the context, kindly state "I don't know." Don't try to make up an answer.

    CONTEXT: {context}

    QUESTION: {question}"""
    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )

    chain = RetrievalQA.from_chain_type(llm=llm,
                                        chain_type="stuff",
                                        retriever=retriever,
                                        input_key="query",
                                        return_source_documents=False,
                                        chain_type_kwargs={"prompt": PROMPT})

    return chain


if __name__ == "__main__":
    create_vector_db()
    chain = get_qa_chain()
    print(chain("How can i debug Kafka Rebalancing issue?"))
    print(chain("Any more suggestions?"))

