from django.contrib import admin
from .models import Usuario,Livro

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    readonly_fields = ('username', 'email', 'password')
    list_display = ('username', 'email')
    search_fields = ('username',)
    list_per_page = int = 15
    model = Usuario

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('id_livro','title','author','publisher','genre')
    search_fields = ('title','author','piblisher','genre',)
    list_per_page = int = 15
    model = Livro