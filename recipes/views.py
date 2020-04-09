from django.shortcuts import render, redirect, reverse
from .models import Recipe
from .forms import RecipeForm

def all_recipes(request):
    recipes = Recipe.objects.all()
    return render(request, "recipes.html", {"recipes": recipes})

def add_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            recipes = Recipe.objects.all()
            return redirect(reverse("recipes"))
    else:
        form = RecipeForm
    return render(request, "recipes_form.html", {"form": form})