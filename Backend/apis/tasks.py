from celery import shared_task
import requests
from .models import GeneratedImage

import os

@shared_task
def generate_image(prompt):
    
    API_URL = os.getenv('STABILITY_AI_API_URL', 'https://api.stability.ai/v2beta/stable-image/generate/core')
    API_KEY = 'sk-cEuKX6oWXLA7oWUEmx1CH1B4jD4Q0buCeiDAYNkzuBpBx6dz'

    headers = {
        'Authorization': f'Bearer {API_KEY}',
        "Accept": "image/*",
    }

    files = {"none": ''}

    output_format = os.getenv('IMAGE_OUTPUT_FORMAT', "webp")
    
    data = {
        "prompt": prompt,
        "output_format": output_format,
    }

    response = requests.post(API_URL, headers=headers, files=files, data=data)

    if response.status_code == 200:
        ## store image in the db
        GeneratedImage.objects.create(prompt=prompt, image_data=response.content, image_encoding=output_format)
        return response.status_code, "Image Generated"
    else:
        return response.status_code, response.json()