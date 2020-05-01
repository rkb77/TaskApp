from django import forms
from django.forms import ModelForm
from Task_App.models import TaskList

class TaskForm(ModelForm):
    class Meta:
        model = TaskList
        fields = "__all__"
