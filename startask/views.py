from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .models import Task, Project
# Create your views here.

class CombinedListView(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all() 
        # context['another_models'] = AnotherModel.objects.all()  
        return context
    
    
class TaskCreateView(CreateView):
    model = Project
    fields = ["name"]
    success_url = reverse_lazy('task_list')
    
# def task_and_project_list(request):
#     tasks = Task.objects.all()
#     projects = Project.objects.all()
#     context = {
#         'tasks': tasks,
#         'projects': projects,
#     }
#     return render(request, 'startask/task_list.html', context)'