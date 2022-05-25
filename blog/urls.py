from django.urls import path
from .views import MenuListView, ViewFood, RecipeListView, index, about

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('<slug:slug>/<slug:food_slug>/', ViewFood.as_view(), name='food_details'),
    path('<slug:slug>/', MenuListView.as_view(), name='menu_list'),
    path('recipe/', RecipeListView.as_view(), name='recipe_list'),

]