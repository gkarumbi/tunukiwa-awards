from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', blank=True,null=True)
    description = models.TextField()
    link = UrlField(max_length=200)

    def __str__(self):
        return self.title

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    def update_project(self):
        self.save()

