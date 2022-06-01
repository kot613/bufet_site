from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView
from .models import Post, Recipe, Comment, Tag, NewsByEmail
from .forms import CommentForm, EmailForm


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context


class RecipeListView(ListView):
    model = Recipe
    template_name = 'blog/recipe_list.html'
    context_object_name = 'recipe_list'

    def get_queryset(self):
        return Recipe.objects.all().order_by('post__category').select_related('post__category')


class MenuViewAll(ListView):
    model = Post
    template_name = 'blog/menu_all.html'
    context_object_name = 'menu_list'

    def get_queryset(self):
        return Post.objects.order_by('category').select_related('category')


class ViewRecipe(DetailView):
    model = Recipe
    template_name = 'blog/recipe_detail.html'
    context_object_name = 'recipe'


class CreateComment(CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.post_id = self.kwargs.get('pk')
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.post.get_absolute_url()


def index(request):
    return render(request, 'base.html')


def about(request):
    return render(request, 'blog/about.html')


class FoodByTag(ListView):
    model = Tag
    template_name = 'blog/tag_list.html'
    context_object_name = 'tag_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Tag.objects.get(slug=self.kwargs['slug'])
        return context

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs['slug']).select_related('category')


class CreateEmail(CreateView):
    model = NewsByEmail
    form_class = EmailForm
    success_url = '/'




