from django.db import models

#Create your models here.
class User(models.Model):
    user = models.CharField(max_length=25, null="False", blank="False")
    email = models.EmailField(max_length=50, null="False", blank="False")
    password = models.CharField(max_length=20)


    def __str__(self):
        return self.user


class Project(models.Model):
    name = models.CharField(max_length=70, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    user = models.ForeignKey(User, models.CASCADE, related_name='projects')


    def __str__(self):
        return self.name


class Task(models.Model):
    STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('finished', 'Finished')
    ]
    title = models.CharField(max_length=80, null=False, blank=False)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True, null=False, blank=False)
    status_completed = models.CharField(max_length=15, choices=STATUS_CHOICES,default="todo")
    project = models.ForeignKey(Project, models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.title


