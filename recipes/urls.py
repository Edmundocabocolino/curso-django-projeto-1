from django.urls import path
from . import  views




urlpatterns = [
    path('', views.home, name='home'),
    path('recipeviews/<int:id>/', views.recipeviews, name='recipe-views'),
    
]