from langchain.document_loaders import TextLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
import os

class RAG:

    def __init__(self, folder) -> None:
        txt_files = [f for f in os.listdir(folder) if f.endswith('.txt')]
        documents = []
        for file in txt_files:
            raw_documents = TextLoader(os.path.join(folder, file)).load()
            text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
            documents.extend(text_splitter.split_documents(raw_documents))
        self.db = FAISS.from_documents(documents, OpenAIEmbeddings(openai_api_key="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"))

    def get_context(self, query):
        embedding_vector = OpenAIEmbeddings(openai_api_key="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").embed_query(query)
        docs = self.db.similarity_search_by_vector(embedding_vector)
        return docs[0].page_content

if __name__ == "__main__":
    query = "What is computer graphics?"
    rag = RAG("../docs/")
    print(rag.get_context(query))
