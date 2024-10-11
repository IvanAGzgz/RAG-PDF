from langchain.chains.question_answering import load_qa_chain
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.prompts import PromptTemplate
import streamlit as st


from dotenv import load_dotenv
import os

CHROMA_PATH = "chroma"

load_dotenv()
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")

def get_conversational_chain():

    prompt_template = """
        Responde a la pregunta con el mayor detalle posible a partir del contexto proporcionado, asegúrate de proporcionar todos los detalles. Si la respuesta no está en el contexto proporcionado, simplemente di: "la respuesta no está disponible en el contexto". No proporciones una respuesta incorrecta.

    Contexto:\n {context}\n
    Pregunta:\n {question}\n

    Respuesta:

    """

    model = ChatOpenAI(temperature=0.3)

    prompt = PromptTemplate(template = prompt_template, input_variables = ["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)

    return chain

def user_input(user_question):
    embeddings = OpenAIEmbeddings()
    
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embeddings)
    docs = db.similarity_search(user_question)

    chain = get_conversational_chain()

    
    response = chain(
        {"input_documents":docs, "question": user_question}
        , return_only_outputs=True)

    print(response)
    st.write("Reply: ", response["output_text"])


def main():
    st.set_page_config("Chat PDF")
    st.header("Chat con OpenAI sobre la Constitucion Española💁")

    user_question = st.text_input("Pregunta:")

    if user_question:
        user_input(user_question)

if __name__ == "__main__":
    main()