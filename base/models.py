from django.db import models

class UserInput(models.Model):
    image = models.ImageField(upload_to='donation_images/')
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    goal = models.IntegerField()
