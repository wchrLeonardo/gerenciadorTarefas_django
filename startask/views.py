from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.shortcuts import get_object_or_404
from .models import Task, Project
# Create your views here.

class CombinedListView(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        project_id = self.request.GET.get('project_id')
        if project_id:
            return Task.objects.filter(project=project_id)
        return Task.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all() 
        context['selected_project_id'] = self.request.GET.get('project_id')
        # context['another_models'] = AnotherModel.objects.all()  
        return context
    
    
class ProjectCreateView(CreateView):
    model = Project
    fields = ["name"]
    success_url = reverse_lazy('task_list')


class TaskCreateView(CreateView):
    model = Task
    fields = ["title", "description"]
    success_url = reverse_lazy("task_list")

    def form_valid(self, form):
        project_id = self.request.POST.get("project_id")
        if project_id:
            project = get_object_or_404(Project, id=project_id)
            form.instance.project = project
        return super().form_valid(form)



    






# def task_and_project_list(request):
#     tasks = Task.objects.all()
#     projects = Project.objects.all()
#     context = {
#         'tasks': tasks,
#         'projects': projects,
#     }
#     return render(request, 'startask/task_list.html', context)'