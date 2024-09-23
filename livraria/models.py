from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=64)

    def __str__(self):
        return self.username

class Livro(models.Model):
    id_livro = models.AutoField(primary_key=True)
    title = models.CharField('Nome',max_length=255)
    author = models.CharField('Autor',max_length=255)
    publisher = models.CharField('Editora',max_length=255)
    genre = models.CharField('Gênero',max_length=255)
    image = models.ImageField('Imagem', upload_to='media/')
    download = models.FileField('URL', upload_to='pdf/')
                            
    
    def __str__(self):
        return self.title