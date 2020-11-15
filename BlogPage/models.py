from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to = 'pics')
    date = models.DateField()
    description = models.TextField(max_length = 200)
    para1 = models.TextField(max_length = 500)
    para2 = models.TextField(max_length = 500)
    highlighter = models.TextField(max_length = 300)
    likes = models.ManyToManyField(User, related_name = "like_blog")
    dislikes = models.ManyToManyField(User, related_name = "dislike_blog")


    def total_likes(self):
        return self.likes.count()



    def __str__(self):
        return self.title 