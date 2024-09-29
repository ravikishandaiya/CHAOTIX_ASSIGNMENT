from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse, JsonResponse, Http404
from django.urls import reverse
# Create your views here.

from celery.result import AsyncResult
import os
from .models import GeneratedImage
from .tasks import generate_image

    

class Generate_image(APIView):
    def get(self, request):
        prompt = request.GET.get('prompt')

        if not prompt:
            return Response({"error": "Missing required parameter: 'prompt'."}, status=status.HTTP_400_BAD_REQUEST)

        image_obj = GeneratedImage.objects.filter(prompt=prompt).order_by('-created_at').first()
        if not image_obj:
            raise Http404("Image not found")

        return HttpResponse(image_obj.image_data, content_type="image/" + image_obj.image_encoding)

    

    def post(self, request):

        prompts = request.data.get('prompts', [])
        
        if not isinstance(prompts, list):
            return JsonResponse({"error": "Prompt must be a list."}, status=status.HTTP_400_BAD_REQUEST)

        # prompts = request.GET.get('prompt', 'A mouse under a lion').split(',')
        print("Prompts:", prompts)

        #image_url = request.build_absolute_uri() + f'?prompt={prompts[0].replace(' ', '%20')}'
        #return JsonResponse({"image_urls": image_url}, status=status.HTTP_200_OK)

        tasks = []
        for prompt in prompts:
            task_id = generate_image.delay(prompt)
            tasks.append(
                {
                    "task_id": task_id,
                    "prompt": prompt
                }
            )

        result = []
        for task in tasks:
            status_code, response = task['task_id'].get()
            temp = {
                    "prompt": task["prompt"],
                    "status_code": status_code
            }

            if status_code == status.HTTP_200_OK:
                print(200)
                # image_obj = GeneratedImage.objects.filter(prompt=temp["prompt"]).order_by('-created_at').first()
                image_url = request.build_absolute_uri() + f'?prompt={task["prompt"].replace(' ', '%20')}'
                temp['url'] = image_url

            else:
                temp["reponse"] = response

            result.append(temp)


        # print(result)

        #if status_code == 200:
        #    return HttpResponse(response, status = status_code)
        #else:
        #   return JsonResponse(response, status = status_code)

        return JsonResponse(result, safe=False) 

