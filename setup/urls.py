from django.contrib import admin
from django.urls import path

from startask.views import CombinedListView, TaskCreateView
# from startask.views import add_project

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", CombinedListView.as_view(), name="task_list"),
    path("add-project/", TaskCreateView.as_view(), name="add_project"),
]

