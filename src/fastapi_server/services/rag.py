from langchain_community.document_loaders import PyMuPDFLoader
from langchain_experimental.text_splitter import SemanticChunker
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma


class RAGService:
    def __init__(self):
        self.file_path = "assets/Insurance Knowledgebase.pdf"
        self.loader = PyMuPDFLoader(self.file_path)
        self.document = self.loader.load()
        self.embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-base-en-v1.5")
        self.text_splitter = SemanticChunker(embeddings=self.embeddings)
        self.split_documents = self.text_splitter.split_documents(self.document)
        self.vector_store = Chroma.from_documents(self.split_documents, self.embeddings)
        self.retriever = self.vector_store.as_retriever()

    def retrieve_docs_only(self, query, top_k=4):
        retrieved_docs = self.retriever.invoke(query, k=top_k)
        return retrieved_docs