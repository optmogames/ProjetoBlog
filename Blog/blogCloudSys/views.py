from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.

def postagem(request, template_name='home.html'):
    postagem = Postagem.objects.all()
    postagens = {'lista': postagem}
    return render(request, template_name, postagens)

def postagem_list(request, pk, template_name='post.html'):
    post = get_object_or_404(Postagem, pk=pk)
    return  render(request, template_name, {'post': post})