from django.contrib import admin
from .models import Category, Recipe

# Register your models he

class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Recipe)

class RecipeAdimin(admin.ModelAdmin):
    ...

admin.site.register(Category,CategoryAdmin)