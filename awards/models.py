from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', blank=True,null=True)
    description = models.TextField()
    link = models.URLField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    def update_project(self):
        self.save()

class Profile(models.Model):
    profile = models.ImageField(upload_to='profiles/', blank=True,null=True)
    bio = models.TextField()
    project = models.ForeignKey(Project, on_delete = models.CASCADE)
    phone = PhoneNumberField()

    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_profile(self):
        self.save()

