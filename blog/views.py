from django.shortcuts import render
from .models import Post

# from django.http import HttpResponse

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

#
# This is a way to render direct HTTP responses.  Considered old style
#

# def about(request):
#     return HttpResponse('<h1>About Home</h1>')
