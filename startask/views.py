from django.shortcuts import render
from .models import Task
from .models import Project
# Create your views here.
def task_list(request):
    tasks = Task.objects.all()
    projects = Project.objects.all()
    return render(request, "startask/task_list.html", {"tasks":tasks,"projects":projects})

