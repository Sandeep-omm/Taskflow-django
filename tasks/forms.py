from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "priority", "due_date", "status"]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "e.g. Prepare project proposal"}),
            "description": forms.Textarea(attrs={"rows": 4, "placeholder": "Add a few details…"}),
            "due_date": forms.DateInput(attrs={"type": "date"}),
        }


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
