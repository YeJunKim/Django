from django.db import models
from django.utils import timezone

"""
models.CharField - Used to define text with a limited number of characters. Use this to store short string information, such as a title.
models.TextField - Property for long text with no limit on the number of characters.
models.DateTimeField - Represents the date and time.
models.ForeignKey - Links to other models.
"""

from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']