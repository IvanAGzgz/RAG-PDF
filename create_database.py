from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
import os
import shutil

CHROMA_PATH = "chroma"
DATA_PATH = "data\Constitucion.pdf"

load_dotenv()
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")

def load_documents():
    loader = PyPDFLoader(DATA_PATH)
    docs = loader.load()
    return docs

def chunks_generator(docs):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 300,chunk_overlap = 100)
    chunks = text_splitter.split_documents(docs)
    print(f"Se han dividido {len(docs)} en {len(chunks)} chunks.")

    document = chunks[10]
    print(document.page_content)
    print(document.metadata)
    return chunks

def save_to_chroma(chunks):
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)

    db = Chroma.from_documents(chunks, OpenAIEmbeddings(),persist_directory=CHROMA_PATH)
    db.persist()
    print(f'Se han guardado {len(chunks)}chunks en {CHROMA_PATH}')

def generar_data_store():
    documents = load_documents()
    chunks = chunks_generator(documents)
    save_to_chroma(chunks)

def main():
    generar_data_store()


if __name__=='__main__':
    main()