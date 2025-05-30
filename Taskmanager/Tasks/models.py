from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class CustomUser(AbstractUser):
    pass



class Task(models.Model):
    STATUS_CHOICES = [('Pending', 'Pending'), ('In Progress', 'In Progress'),
                      ('Completed', 'Completed'), ('Deferred', 'Deferred')]
    PRIORITY_CHOICES = [('Low', 'Low'), ('Medium', 'Medium'),
                        ('High', 'High'), ('Critical', 'Critical')]
    CATEGORY_CHOICES = [('Work', 'Work'), ('Personal', 'Personal'),
                        ('Home', 'Home'), ('Study', 'Study'), ('Others', 'Others')]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

