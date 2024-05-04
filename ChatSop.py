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

instructor_embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
llm = GoogleGenerativeAI(model="models/text-bison-001", google_api_key="<>")
vectordb_file_path = "faiss_index"

def create_vector_db():
    loader = CSVLoader(file_path='SOP.csv')
    data = loader.load()

    vectordb = FAISS.from_documents(documents=data, embedding=instructor_embeddings)
    vectordb.save_local(vectordb_file_path)

def get_qa_chain():
    vectordb = FAISS.load_local(vectordb_file_path, instructor_embeddings, allow_dangerous_deserialization=True)
    retriever = vectordb.as_retriever(score_threshold=1.0)

    prompt_template = """Given the following context and a question, generate an answer based on this context only.
    In the answer try to provide as much text as possible from "SOP Title","SOP Description" and "SOP Steps"  section in the source document context without making much changes.
    If the answer is not found in the context, kindly state "I don't know." Don't try to make up an answer just give slight hint in few sentences but at end mention to reach out to Seniors to get more details on your queries.

    CONTEXT: {context}

    QUESTION: {question}"""
    PROMPT = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

    chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever, input_key="query", return_source_documents=False, chain_type_kwargs={"prompt": PROMPT})

    return chain

def chat_search():
    chain = get_qa_chain()
    while True:
        user_input = input("Get SOP information on: ")
        response = chain(user_input)
        result = response['result']
        print("\n".join(f"* {r}" for r in result.split("\n")))

if __name__ == "__main__":
    create_vector_db()
    chat_search()