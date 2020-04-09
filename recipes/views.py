from django.shortcuts import render, redirect, reverse, get_object_or_404
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

def recipe_detail(request, pk):
    """
    Create a view that returns a single
    Post object based on the post ID (pk) and
    render it to the 'postdetail.html' template.
    Or return a 404 error if the post is
    not found
    """
    recipe = get_object_or_404(Recipe, pk=pk)
    recipe.save()
    return render(request, "recipedetail.html", {'recipe': recipe})