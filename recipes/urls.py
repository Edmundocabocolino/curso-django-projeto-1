from django.urls import path
from . import  views



urlpatterns = [
    path('', views.home),
    path('recipeviews/<int:id>/', views.recipeviews, name='recipeviews'),
    path('cachorroview/<int:id>/', views.yorkshire, name='yorkshire'),
    path('miniminviews/<int:id>/', views.miniminviews, name='miniminviews'),
    path('ursoviews/<int:id>/', views.ursoviews, name='ursoviews'),
    path('dotoraviews/<int:id>/', views.dotoraviews, name='dotoraviews'),
    path('shitzuviews/<int:id>/', views.shitzuviews, name='shitzuviews'),
    path('ovelhinhaviews/<int:id>/', views.ovelhinhaviews, name='ovelhinhaviews'),
]