from django.contrib import admin
from django.urls import path

from startask.views import task_list
# from startask.views import add_project

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", task_list),
    # path("", add_project),
]
