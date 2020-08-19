from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from vote.models import VoteModel
from vote.managers import VotableManager


# Create your models here.
class Project(VoteModel,models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', blank=True,null=True)
    description = models.TextField()
    link = models.URLField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)
    upvote = models.PositiveIntegerField(default=0)
    downvote = models.PositiveIntegerField(default=0)
    id = models.OneToOneField('Profile', on_delete=models.CASCADE, primary_key=True)

    User.profile = property(lambda u: Profile.objects.get_or_create(user=u)[0])

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:

        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):

    instance.profile.save()

    def __str__(self):
        return self.user.username


    def __str__(self):
        return self.title

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    def update_project(self):
        self.save()

    @classmethod
    def get_single_project(cls,pk):
        project = cls.objects.get(pk = pk)
        return project 

class Profile(models.Model):
    profile = models.ImageField(upload_to='profiles/', blank=True,null=True)
    bio = models.TextField()
    #project = models.ForeignKey(Project, on_delete = models.CASCADE)
    id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone = PhoneNumberField()

    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_profile(self):
        self.save()

