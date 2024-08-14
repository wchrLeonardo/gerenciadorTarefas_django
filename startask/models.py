from django.db import models

#Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=70, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=80, null=False, blank=False)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True, null=False, blank=False)
    completed = models.BooleanField(default=False)
    project = models.ForeignKey(Project, models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.title


