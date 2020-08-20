from django import forms
from .models import Project, Profile

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title','image','description','link']
        exclude =['pub_date']
        #exclude = ['pub_date','upvote','downvote','user']

class ProfileForm(forms.ModelForm):
    class Meta:
        model= Profile
        fields = ['profile','bio','phone']
        #exclude = ['id']