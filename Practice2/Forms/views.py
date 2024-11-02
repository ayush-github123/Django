from django.shortcuts import render, redirect, get_object_or_404
from Forms.models import Recipe
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


def submit(request):
    if request.method == 'POST':
        recipe_name = request.POST['recipeName']
        recipe_desc = request.POST['recipeDesc']
        recipe_category = request.POST['category']

        recipe = Recipe.objects.create(recipe_name=recipe_name, recipe_description=recipe_desc, recipe_category=recipe_category)
        recipe.save()

        messages.success(request, 'Recipe added successfully...')

        return redirect('/')

    else:
        return redirect('/')
    

def display(request):
    recipes = Recipe.objects.all().order_by('-created_at')

    return render(request, 'display.html', {'recipes':recipes})


def search(request):
    search = request.GET['search']
    recipes = Recipe.objects.filter(recipe_name__iexact=search)

    return render(request, 'search.html', {'recipes':recipes})

def delete_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    if request.method == 'POST':
        recipe.delete()
    return redirect('display')
