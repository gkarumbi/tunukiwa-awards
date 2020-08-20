from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .models import Project,Profile
from .forms import ProjectForm,ProfileForm
from vote.managers import VotableManager
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  MoringaMerch
from .serializer import ProjectSerializer, ProfileSerializer


# Create votes object
votes = VotableManager()

def index(request):
    current_user = request.user
    projects = Project.objects.all()

    return render(request, 'index.html',{'projects':projects, 'user':current_user})

@login_required(login_url='accounts/login')
def profile(request,username):
    user = request.user 
    profile = Profile.objects.get(pk=user.id)
    print(profile)
    return render(request, "profile.html",{'user':user,'profile':profile})


@login_required(login_url='accounts/login')
def create_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()

        return redirect('/')
    else:
        form = ProjectForm()

    return  render(request,"create_project.html",{'form':form})

@login_required(login_url='accounts/login')
def create_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            messages.success(request, ('Your profile was successfully created!'))

        return redirect('/')
    else:
        messages.error(request, ('Please correct the error below.'))
        form = ProfileForm()

    return  render(request,"create_profile.html",{'form':form})


@login_required(login_url='accounts/login')
def like_project(request,pk):
    project = Project.get_single_project(pk)
    current_user = request.user
    user_id = current_user.id

    if current_user.is_authenticated:
        upvote = project.votes.up(user_id)
        print(upvote)
        project.upvote = project.votes.count()
        project.save()

    return redirect('/')


@login_required(login_url='accounts/login')
def dislike_project(request,pk):
    project = Project.get_single_project(pk)
    current_user = request.user
    user_id = current_user.id

    if current_user.is_authenticated:
        downvote = project.votes.down(user_id)
        print(project.id)
        print(downvote)
        print(project.vote_score)
        project.downvote = project.votes.count()

    return redirect('/')

class ProjectList(APIView):
    def get(self, request,format=None)
    all_projects = Project.objects.all()
    serializers = ProjectSerializer(all_projects,many=True)
    response Response(serializers.data)

class ProfileList(APIView):
    def get(self, request,format=None)
    all_profiles = Profile.objects.all()
    serializers = ProfileSerializer(all_profile,many=True)
    response Response(serializers.data)

