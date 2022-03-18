from django.forms import ModelForm
from .models import *
class Todoform(ModelForm):
    class Meta:
        model = Todo
        fields = ['title' , 'memo' , 'importan']
