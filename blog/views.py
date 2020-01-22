from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


# Create your views here.
def index(request):
    # return HttpResponse("Hey there! :)")
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})


def post(request):
    return HttpResponse("I am a single post page. ;)")