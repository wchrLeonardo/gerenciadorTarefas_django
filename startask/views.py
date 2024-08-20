from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.views.generic.edit import UpdateView
from django.shortcuts import get_object_or_404, redirect
from .models import Task, Project, User
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from django.contrib.auth.views import LoginView
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate


class CombinedListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'


    def get_queryset(self):
        project_id = self.request.GET.get('project_id')
        if project_id:
            print(f"User instance: {self.request.user} (Type: {type(self.request.user)})")
            return Task.objects.filter(project_id=project_id, project__user=self.request.user)
        return Task.objects.filter(project__user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Exibe apenas projetos associados ao usuário logado
        context['projects'] = Project.objects.filter(user=self.request.user)
        context['selected_project_id'] = self.request.GET.get('project_id')
        return context

    
    
class ProjectCreateView(CreateView):
    model = Project
    fields = ["name"]
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('task_list')


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
    

class UpdateTaskView(UpdateView):
    model = Task
    fields = ['title', 'description'] 
    template_name = 'startask/task_update.html'
    context_object_name = 'task'
    
    def get_success_url(self):
        project_id = self.object.project.id  
        return reverse('task_list')+ f'?project_id={project_id}'
    


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


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    project_id = request.GET.get('project_id')  
    task.delete()
    if project_id:
        url = f"{reverse('task_list')}?project_id={project_id}"
        return redirect(url)  
    return redirect(reverse('task_list'))


def delete_project(request):
    project_id = request.GET.get('project_id')
    project = get_object_or_404(Project, id=project_id)
    if project_id:
        project.delete()
        return redirect(reverse('task_list'))
    else:
        return JsonResponse({'success': False, 'error': 'error'})
 

from django.contrib import messages
from .forms import RegisterForm, LoginForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
       
            auth_login(request, user)  
            return redirect(reverse('task_list'))  
    else:
        form = RegisterForm()

    return render(request, 'startask/register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect(reverse('task_list'))  
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        form = LoginForm()
    
    return render(request, 'startask/login.html', {'form': form})
