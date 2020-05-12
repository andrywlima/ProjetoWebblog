from django.shortcuts import render, redirect
from .models import Post
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})


def login_user(request):
    return render(request, 'login.html')


@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Usuário e senha inválidos, Favor entrar novamente, ou então, cadastre-se!')
    return redirect('/login/')


def logout_user(request):
    print(request.user)
    logout(request)
    return redirect('/login/')
