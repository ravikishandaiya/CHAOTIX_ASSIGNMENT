from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse


class Index(APIView):
    def get(self, request):
        
        html = """
                    <!DOCTYPE html>
                    <html lang="en">
                        <head>
                            <meta charset="UTF-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1.0">
                            <title>Text To Image</title>
                            <style>
                                body {
                                    text-align: center;
                                    font-family: Arial, sans-serif;
                                }
                            </style>
                        </head>
                        <body>
                            <h1>Text To Image Generator</h1>
                            <p>Implementation in process</p>
                            
                            <a href = "/apis/">Go to the API</a>
                        </body>
                    </html>

                """
        
        return HttpResponse(html)