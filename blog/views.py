from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

from blog.forms import PostForm
from blog.models import Categoria, Post


def home(request):

    name = "Álef"

    #categorias = ['PHP', 'Java', 'c/c++']
    #for categoria in categorias:
        #Categoria.objects.create(name=categoria)
    todas_categorias = Categoria.objects.all()

    #categoria_python = Categoria.objects.get(name=name)
    posts = Post.objects.filter(statu='Published')

    #post = Post()
    #post.name = "Show Post 3"
    #post.content = "Content"
    #post.statu = "Published"
    #post.categoria = categoria_python
    #post.save()

    context = {
        'name': name,
        'categorias': todas_categorias,
        'posts': posts,
    }

    return render(request, 'blog/index.html', context)

def show_posts_by_category(request, categoria_id):
    name = "Álef"
    todas_categorias = Categoria.objects.all()
    categoria = Categoria.objects.get(pk=categoria_id)
    posts = Post.objects.filter(categoria=categoria, statu='Published')

    context = {
        'name': name,
        'posts': posts,
        'categorias': todas_categorias,
        'categoria': categoria,
    }

    return render(request, 'blog/index.html', context)

def auth(request):
    error = False
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user == None:
            error = True
        else:
            error = False
            login(request, user)

    context = {
        "error": error
    }
    return render(request, 'blog/auth.html', context)

def logout_view(request):
    logout(request)
    return redirect('/blog')

def post_create(request):
    form = PostForm()
    return render(request, 'blog/post_create.html', {'form':form})
