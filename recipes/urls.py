from django.conf.urls import url
from .views import all_recipes, add_recipe, recipe_detail


urlpatterns = [
    url(r'^$', all_recipes, name="recipes"),
    url(r'^new/$', add_recipe, name="add_recipe"),
    url(r'^(?P<pk>\d+)/$', recipe_detail, name='recipe_detail'),
]