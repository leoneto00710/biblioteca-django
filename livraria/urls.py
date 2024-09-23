from django.urls import path
from . import views


urlpatterns = [
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('login/', views.login, name='login'),
    path('validar_cadastro/', views.validar_cadastro, name='validar_cadastro'),
    path('validar_login/', views.validar_login, name='validar_login'),
    path('sair/', views.sair, name='sair'),
    path('app/', views.app, name='app'),
]

