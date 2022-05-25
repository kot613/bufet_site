from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
from ckeditor.fields import RichTextField




class Category(MPTTModel):
    name = models.CharField(max_length=100, verbose_name='Название категории', db_index=True)
    slug = models.SlugField(max_length=100, unique=True, verbose_name='URL категории', db_index=True)
    image = models.ImageField(upload_to='category/', verbose_name='Миниатюра')
    parent = TreeForeignKey('self', related_name='children', on_delete=models.SET_NULL, null=True, blank=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})


class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название тега', db_index=True)
    slug = models.SlugField(max_length=100, unique=True, verbose_name='URL тега', db_index=True)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tag', kwargs={'slug': self.slug})


class Post(models.Model):
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE, verbose_name='Автор поста')
    title = models.CharField(max_length=250, verbose_name='Название поста', db_index=True)
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL поста', db_index=True)
    image = models.ImageField(upload_to='articles/', verbose_name='Миниатюра')
    text = models.TextField(verbose_name='Текст')
    category = models.ForeignKey(Category,
                                 related_name='post', on_delete=models.SET_NULL, null=True, verbose_name='Категория')
    tags = models.ManyToManyField(Tag, related_name='post', verbose_name='Теги')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    price = models.CharField(max_length=50, verbose_name='Стоимость')
    width = models.CharField(max_length=50, verbose_name='Вес')
    calories = models.CharField(max_length=50, verbose_name='Калорийность')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Постьі'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('food_details', kwargs={"slug": self.category.slug, "food_slug": self.slug})


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    serves = models.CharField(max_length=50)
    prep_time = models.PositiveIntegerField(default=0)
    cook_time = models.PositiveIntegerField(default=0)
    ingredients = RichTextField()
    directions = RichTextField()
    post = models.ForeignKey(Post, related_name='recipe', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецептьі'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('recipe_details', kwargs={"pk": self.pk})


class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    message = models.TextField(max_length=500)
    post = models.ForeignKey(Post, related_name='comment', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Комент'
        verbose_name_plural = 'Коментьі'





