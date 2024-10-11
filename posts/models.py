from django.db import models

# Create your models here.
class Posts(models.Model):
    title=models.CharField(max_length=50)
    viewe=models.CharField(max_length=50)
    content=models.TextField()
    date =models.DateTimeField(null=True,blank=True)
    author=models.CharField(max_length=50)
    category=models.CharField(max_length=50)