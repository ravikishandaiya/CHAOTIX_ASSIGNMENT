from django.db import models

# Create your models here.
class GeneratedImage(models.Model):
    prompt = models.TextField() 
    image_data = models.BinaryField()  
    image_encoding = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    