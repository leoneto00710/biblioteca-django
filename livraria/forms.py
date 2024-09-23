from django import forms 
from django.db.models import fields
from .models import Livro

class CadastroLivro(forms.ModelForm):
    class Meta:
        model = Livro
        fields= "__all__"