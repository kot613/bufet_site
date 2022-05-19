from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView
from .models import Post, Category, Recipe


class MenuListView(ListView):
    model = Post
    template_name = 'blog/menu_list.html'
    context_object_name = 'menu_list'

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs.get('slug')).select_related('category')


class ViewFood(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    slug_url_kwarg = 'food_slug'
    context_object_name = 'food'


class RecipeListView(ListView):
    model = Recipe
    template_name = 'blog/recipe_list.html'
    context_object_name = 'recipe_list'




def home(request):
    return render(request, 'base.html')
