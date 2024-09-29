from django.urls import path

from . import views

urlpatterns = [
    path('', views.Generate_image.as_view(), name='text_to_image_api'),
]