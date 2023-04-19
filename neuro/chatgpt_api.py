import openai
import tiktoken
from decouple import config

from handlers import chatgpt

openai.api_key = config('openai_token',default='')

def generate_answer(prompt, user_id):
    encoding = tiktoken.encoding_for_model('gpt-3.5-turbo-0301')
    num_tokens = len(encoding.encode(prompt))
    chatgpt.tokens += chatgpt.tokens + num_tokens
    if chatgpt.tokens > 500:
        chatgpt.messages.pop(0)
    
    chatgpt.messages.append({'role': 'user', 'content': prompt})
    completion = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=chatgpt.messages,
        max_tokens=500,
        user=str(user_id)
    )
    answer = completion.choices[0].message.content
    chatgpt.messages.append({'role': 'assistant', 'content': answer})
    return answer
