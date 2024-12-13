import os

from dotenv import load_dotenv
from langchain_community import DirectoryLoader, UnstructuredPDFLoader
from langchain_community import PGVector
from langchain_experimental import SemanticChunker
from langchain_openai import OpenAIEmbeddings

load_dotenv()

loader = DirectoryLoader(
    os.path.abspath("../pdf-documents"),
    glob="**/*.pdf",
    use_multithreading=True,
    show_progress=True,
    max_concurrency=50,
    loader_cls=UnstructuredPDFLoader,
)
docs = loader.load()

embeddings = OpenAIEmbeddings(model='text-embedding-ada-002', )

text_splitter = SemanticChunker(
    embeddings=embeddings
)

flattened_docs = [doc[0] for doc in docs if doc]
chunks = text_splitter.split_documents(flattened_docs)

PGVector.from_documents(
    documents=chunks,
    embedding=embeddings,
    collection_name="collection164",
    connection_string="postgresql+psycopg://postgres@localhost:5432/database164",
    pre_delete_collection=True,
)