from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'recipes/page/home.html')

def recipeviews(request, id):
    return render(request, "recipes/page/recipeviews.html")

def yorkshire(request, id):
    return render(request, "recipes/page/cachorroview.html")

def miniminviews(request, id):
    return render(request, "recipes/page/miniminviews.html")

def ursoviews(request, id):
    return render(request, "recipes/page/ursoviews.html")

def dotoraviews(request, id):
    return render(request, "recipes/page/dotoraviews.html")

def shitzuviews(request, id):
    return render(request, "recipes/page/shitzuviews.html")

def ovelhinhaviews(request, id):
    return render(request, "recipes/page/ovelhinhaviews.html")

