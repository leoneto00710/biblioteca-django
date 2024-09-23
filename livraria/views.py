from django.http.response import HttpResponse
from django.db.models import Q
from django.shortcuts import render
from django.shortcuts import redirect
from hashlib import sha256
from .models import Usuario,Livro


def login(request):
    status = request.GET.get('status')
    return render(request, 'cadastro/login.html', {'status':status})

def cadastrar(request):
    status = request.GET.get('status')
    return render(request, 'cadastro/cadastrar.html', {'status':status})

def validar_cadastro(request):
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    
    usuario = Usuario.objects.filter(email=email)

    if len(username.strip())==0 or len(email.strip())==0:
       return redirect('/cadastrar/?status=1') 
    
    if len(password)<8:
       return redirect('/cadastrar/?status=2') 

    if len(usuario)>0:
       return redirect('/cadastrar/?status=3') 
    try:
        password = sha256(password.encode()).hexdigest()
        usuario = Usuario(username=username,email=email,password=password)
        usuario.save()
        return redirect('/cadastrar/?status=0') 
    except:
       return redirect('/cadastrar/?status=4') 
    
def validar_login(request):
    email=request.POST.get('email')
    password=request.POST.get('password')

    password=sha256(password.encode()).hexdigest()

    usuario=Usuario.objects.filter(email=email).filter(password=password)

    if len(usuario) == 0:
        return redirect('/login/?status=1')
    elif len(usuario) > 0:
        request.session['usuario'] = usuario[0].id_usuario
        return redirect(f"/app/?id_usuario={request.session['usuario']}")

def sair(request):
    request.session.flush()
    return redirect('/login')

def app(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id_usuario=request.session['usuario'])
        livros = Livro.objects.all()
        return render(request, 'app.html', {'livros': livros})
    else:
        return redirect('/login/?status=2')
    