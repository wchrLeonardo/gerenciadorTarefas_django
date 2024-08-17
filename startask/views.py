from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.shortcuts import get_object_or_404, redirect
from .models import Task, Project
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
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


# def update_task_status(request, task_id, status):
#     task = get_object_or_404(Task, id=task_id)
#     if status in ['todo', 'in_progress', 'finished']:
#         task.status_completed = status
#         task.save()
#         return JsonResponse({'success': True})
#     return JsonResponse({'success': False, 'error': 'Status inválido'})
    
def update_task_status(request, task_id, status):
    task = get_object_or_404(Task, id=task_id)
    if status in ['todo', 'in_progress', 'finished']:
        task.status_completed = status
        task.save()
        project_id = request.GET.get('project_id')
        if project_id:
            url = f"{reverse('task_list')}?project_id={project_id}"
            return redirect(url)  
        return redirect(reverse('task_list'))
    return JsonResponse({'success': False, 'error': 'Status inválido'})




