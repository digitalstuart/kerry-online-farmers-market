from django.conf.urls import url
from .views import all_recipes, add_recipe


urlpatterns = [
    url(r'^$', all_recipes, name="recipes"),
    url(r'^new/$', add_recipe, name="add_recipe"),
]