from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Project
from .forms import ProjectForm

# Create your views here.

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

