# Generated by Django 5.0.6 on 2024-06-05 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livraria', '0009_delete_livro'),
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id_livro', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, verbose_name='Nome: ')),
                ('author', models.CharField(max_length=255, verbose_name='Autor: ')),
                ('genre', models.CharField(max_length=255, verbose_name='Gênero: ')),
                ('category', models.CharField(max_length=255, verbose_name='Categoria: ')),
                ('image', models.ImageField(upload_to='media/', verbose_name='Imagem')),
                ('download', models.URLField(verbose_name='URL: ')),
            ],
        ),
    ]
