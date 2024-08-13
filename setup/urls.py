from django.contrib import admin
from django.urls import path

from startask.views import task_list

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", task_list),
]
