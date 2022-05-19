from django.urls import path
from .views import MenuListView, ViewFood, RecipeListView, home

urlpatterns = [
    path('', home),
    path('<slug:slug>/<slug:food_slug>/', ViewFood.as_view(), name='food_details'),
    path('<slug:slug>/', MenuListView.as_view(), name='menu_list'),
    path('<int:pk>/', RecipeListView.as_view(), name='recipe_list'),

]