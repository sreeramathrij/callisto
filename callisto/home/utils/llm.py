import requests
import os
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

class LLM:
    def model_pool(self, name):
        models = {
            "gpt-4" : {
                'name' : 'gpt-4',
                'data' : {"model": "gpt-4", "temperature": 1, "top_p": 1, "n": 1, "max_tokens": 1024, "stream": False, "presence_penalty": 0, "frequency_penalty": 0},
                'url'  : "https://api.openai.com/v1/chat/completions",
                'headers' : {'correlationId': "<Random-GUID>", 'Content-Type': 'application/json'},
                'message-field' : "messages"
            },
            "gpt-4-0613" : {
                'name' : 'gpt-4-0613',
                'data' : {"model": "gpt-4-0613", "temperature": 1, "top_p": 1, "n": 1, "max_tokens": 1024, "stream": False, "presence_penalty": 0, "frequency_penalty": 0},
                'url'  : "https://api.openai.com/v1/chat/completions",
                'headers' : {'correlationId': "<Random-GUID>", 'Content-Type': 'application/json'},
                'message-field' : "messages"
            },
            "gpt-4-0314" : {
                'name' : 'gpt-4-0314',
                'data' : {"model": "gpt-4-0314", "temperature": 1, "top_p": 1, "n": 1, "max_tokens": 1024, "stream": False, "presence_penalty": 0, "frequency_penalty": 0},
                'url'  : "https://api.openai.com/v1/chat/completions",
                'headers' : {'correlationId': "<Random-GUID>", 'Content-Type': 'application/json'},
                'message-field' : "messages"
            },
            "gpt-3.5-turbo-0613" : {
                'name' : 'gpt-3.5-turbo-0613',
                'data' : {"model": "gpt-3.5-turbo-0613", "temperature": 1, "top_p": 1, "n": 1, "max_tokens": 1024, "stream": False, "presence_penalty": 0, "frequency_penalty": 0},
                'url'  : "https://api.openai.com/v1/chat/completions",
                'headers' : {'correlationId': "<Random-GUID>", 'Content-Type': 'application/json'},
                'message-field' : "messages"
            }
        }
        return models[name]

    def __init__(self, model_name, api_key='', params = {}) -> None:
        self.model = self.model_pool(model_name)
        self.data = self.model['data'].copy()
        self.headers = self.model['headers'].copy()
        self.url = self.model['url']
        self.data.update(params)
        self.headers.update({'Authorization': f'Bearer {api_key}'})
        
    def create_message(self, query):
        if not isinstance(query, list):
            query = [('system', "You are a helpful, respectful and honest assistant trained to help computer science engineering college students learn subjects. Always answer as helpfully as possible, while being safe. If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. Answer every question with detailed explainations."),
                     ('user', query)]
        messages = []
        for role, text in query:
            message = {"role" : role, "content": text}
            messages.append(message)
        return messages
    
    def generate(self, query):
        messages = self.create_message(query)
        self.data[self.model['message-field']] = messages
        x = requests.post(self.url, headers=self.headers, json=self.data)
        if x.status_code == 200:
            return x.json()['choices'][0]['message']['content']
        else:
            return x.json()

if __name__ == "__main__":
    gpt4 = LLM("gpt-4", api_key=openai_api_key) #DONT UPLOAD THIS ANYWHERE WITHOUT DELETING THE API KEYS
    gpt40613 = LLM("gpt-4-0613", api_key=openai_api_key) #DONT UPLOAD THIS ANYWHERE WITHOUT DELETING THE API KEYS
    print(gpt4.generate("hey who are you"))
    print(gpt40613.generate([('system', 'You are Nvidia CEO Jenson Huang'),('user', "hey who are you")]))