from django.shortcuts import render
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
import os
from dotenv import load_dotenv
from .utils.llm import LLM
from .utils.rag import RAG
from .utils.prompts import PromptBuilder

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# rag = RAG(api_key=openai_api_key, folder="C:\Projects\callisto\callisto\callisto\home\docs")
# llm = LLM("gpt-4", api_key=openai_api_key)

# Create your views here.
def home(request):
    return render(request, "home/home.html")

def index(request):
    
    # if request.method == 'POST':
    #     query = request.POST.get('textfield', None)
    # else:
    #     return render(request, 'home/index.html')
    
    # context = rag.get_context(query)

    # talk_to_textbook = PromptBuilder([
    #             ('system', "You are a helpful, respectful and honest assistant named {name} trained to help computer science engineering college students learn subjects. Always answer as helpfully as possible, while being safe. If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. Answer every question with detailed explainations."),
    #             ("user", "Imagine you are the textbook : {textbook} teaching students {subject}. Create an answer for the question worth some marks using the provided context from the textbook, where it is delimited by <question>question</question> \n <mark>mark</mark> \n <context>context</context>. Also explain how each line of the answer is worth so the student can understand its importantance. Always answer in a fun and engaging way to provide as much value as possible to the student."),
    #             ("assistant", "Understood! Im the textbook {textbook} teaching students the subject {subject}. I shall answer the question following the guidelines and by being engaging and fun. I will properly tell why each paragraph/line in the answer is worth how much marks. Please provide the question mark and context."),
    #             ("user", "<question>{question}</question> \n <mark>{mark}</mark> \n <context>{context}</context>"),
    #         ])

    # messages = talk_to_textbook.format_messages(name="Bobby", textbook="Principles of Computer Graphics", subject="Computer Graphics", question=query, context=context, mark="5")

    # answer = llm.generate(messages)
    return render(request, "home/base.html")
    