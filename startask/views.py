from django.shortcuts import render
from django.views.generic import ListView, CreateView

from .models import Task
from .models import Project
# Create your views here.
#Só estou mandando as tasks
class TaskListView(ListView):
    model = Task
    
    
class TaskCreateView(CreateView):
    model = Project
    fields = ["name"]
    