from django.contrib import admin
from django.urls import path

from startask.views import CombinedListView, ProjectCreateView, TaskCreateView, update_task_status
# from startask.views import add_project

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", CombinedListView.as_view(), name="task_list"),
    path("add-project/", ProjectCreateView.as_view(), name="add_project"),
    path("add-task/", TaskCreateView.as_view(), name="add_task"),
    path("update-task-status/<int:task_id>/<str:status>/", update_task_status, name="update_task_status"),
]

