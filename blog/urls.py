from django.urls import path
from .views import MenuListView, ViewFood, RecipeListView, ViewRecipe, index, about

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('recipe_all/', RecipeListView.as_view(), name='recipe'),
    path('recipe_all/<int:pk>', ViewRecipe.as_view(), name='recipe_details'),
    path('<slug:slug>/<slug:food_slug>/', ViewFood.as_view(), name='food_details'),
    path('<slug:slug>/', MenuListView.as_view(), name='menu_list'),


]