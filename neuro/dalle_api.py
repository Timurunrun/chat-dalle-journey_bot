import openai
from decouple import config

openai.api_key = config('openai_token',default='')

def generate_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        model='image-alpha-001',
        size='1024x1024',
        response_format='url'
    )
    return(response['data'][0]['url'])
