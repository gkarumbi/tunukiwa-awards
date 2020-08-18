from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Project,Profile
from .forms import ProjectForm,ProfileForm
from vote.managers import VotableManager

# Create votes object
votes = VotableManager()

def index(request):

    return render(request, 'index.html')

@login_required(login_url='accounts/login')
def create_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProjectForm(request.POST)
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
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()

        return redirect('/')
    else:
        form = ProfileForm()

    return  render(request,"create_profile.html",{'form':form})


@login_required(login_url='accounts/login')
def like_project(request,pk):
    project = Project.get_single_project(pk)
    current_user = request.user
    user_id = current_user.id

    if user.is_authenticated:
        upvote = project.votes.up(user_id)
        print(upvote)
        project.upvote = project.votes.count()
        project.save()

    return redirect('/')





