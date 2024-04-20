from django.http import HttpResponse
from django.shortcuts import render
from utils.recipes.factory import make_recipe
from recipes.models import Recipe


from .models import Recipe

# Create your views here.
def home(request):
    recipes = Recipe.objects.all().order_by('-id')
    return render(request,'recipes/page/home.html',context={
        'recipes':recipes,
    })

def recipeviews(request, id):
    return render(request, "recipes/page/recipe-views.html",context={
        
        'is_detail_page': True,
    })


