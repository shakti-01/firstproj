from django.shortcuts import render
from django.http import HttpResponse
from . models import Post

# Create your views here.

""" posts = [
{
    'author': 'Amitabh',
    'title': 'Blog post 1',
    'content': 'Photography is very difficult...',
    'date_posted': 'October 30, 2013'
},
{
    'author': 'Andrew',
    'title': 'Blog post 2',
    'content': 'Politics are rampant these days...',
    'date_posted': 'january 30, 2003'
},
{
    'author': 'James',
    'title': 'Blog post 3',
    'content': 'C++ is faster than bolt...',
    'date_posted': 'July 20, 2015'
}
] """



def index(request):
    context = {'p': Post.objects.all()}
    return render(request, 'mainindex/home.html',context)

def about(request):
    return render(request, 'mainindex/about.html', {'title': 'About'})