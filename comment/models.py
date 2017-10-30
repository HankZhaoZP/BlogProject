from django.db import models

# Create your models here.
class Comment(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=100)
    url=models.URLField(blank=True)
    text=models.TextField()
    create_time=models.DateField(auto_now_add=True)
    post=models.ForeignKey('blog.Post')
