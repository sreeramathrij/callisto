from utils.llm import LLM
from utils.rag import RAG

rag = RAG("./docs/")
llm = LLM("gpt-3.5-turbo-0613", api_key="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")

query = "What is computer graphics?"
context = rag.get_context(query)
new_query = f'{query} \nthis is context: {context}'

print(llm.generate(new_query))