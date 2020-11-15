from django.db import models

# Create your models here.

class Courses(models.Model):
    cour_name = models.CharField(max_length=50)
    cour_link = models.URLField(max_length=100)
    cour_desc = models.CharField(max_length=100)
    cour_star = models.FloatField(default=None)
    cour_price = models.IntegerField(default=None)

    def __str__(self):
        return self.cour_name
     


