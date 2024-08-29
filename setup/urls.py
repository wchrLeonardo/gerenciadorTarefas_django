from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from startask import views
from django.contrib.auth.views import LogoutView
from startask.views import CombinedListView, ProjectCreateView, TaskCreateView, update_task_status, delete_task, delete_project, UpdateTaskView, register, login

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", CombinedListView.as_view(), name="task_list"),
    path("add-project/", ProjectCreateView.as_view(), name="add_project"),
    path("add-task/", TaskCreateView.as_view(), name="add_task"),
    path("update-task-status/<int:task_id>/<str:status>/", update_task_status, name="update_task_status"),
    path('delete-task/<int:task_id>/', delete_task, name="delete_task"),
    path('delete-project/', delete_project,  name="delete_project"),
    path('update-task/<int:pk>/', UpdateTaskView.as_view(), name='update_task'),
    path('login/', views.login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
#     path('register/', views.register, name='register'),
    path('', include('startask.urls')),
 ]

