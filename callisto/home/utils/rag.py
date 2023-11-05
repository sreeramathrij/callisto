from langchain.document_loaders import TextLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
import os
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

class RAG:

    def __init__(self, api_key, folder) -> None:
        txt_files = [f for f in os.listdir(folder) if f.endswith('.txt')]
        self.openai_embed = OpenAIEmbeddings(openai_api_key=api_key)
        documents = []
        for file in txt_files:
            raw_documents = TextLoader(os.path.join(folder, file)).load()
            text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
            documents.extend(text_splitter.split_documents(raw_documents))
        self.db = FAISS.from_documents(documents, self.openai_embed)

    def get_context(self, query):
        embedding_vector = self.openai_embed.embed_query(query)
        docs = self.db.similarity_search_by_vector(embedding_vector)
        context = ''
        for doc in docs:
            context += doc.page_content
            
        return context

if __name__ == "__main__":
    query = "What is computer graphics?"
    rag = RAG(api_key=openai_api_key, folder="./docs/")
    print(rag.get_context(query))