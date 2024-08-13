from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=80, null=False, blank=False)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True, null=False, blank=False)
    completed = models.BooleanField(default=False)
