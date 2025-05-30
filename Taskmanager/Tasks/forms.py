from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Task

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['user', 'created_at', 'updated_at']