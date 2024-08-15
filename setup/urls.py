from django.contrib import admin
from django.urls import path

from startask.views import TaskListView, TaskCreateView
# from startask.views import add_project

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TaskListView.as_view()),
    path("create", TaskCreateView.as_view()),
]

