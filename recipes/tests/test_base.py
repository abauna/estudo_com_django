
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import resolve, reverse

from recipes import views
from recipes.models import Category, Recipe

class Recipe_test_base(TestCase):
    def setUp(self) -> None:
        category = Category.objects.create(name='test')
        author = User.objects.create(
            first_name='user',
            last_name='user',
            username='user',
            password='user',
            email='user',
        )
        recipe = Recipe.objects.create(
            category=category,
            author=author,
            title='teste34',
            description='teste',
            slug='teste',
            preparation=5,
            preparation_time_unit='teste',
            servings=5,
            servings_unit='teste',
            preparation_steps='teste',
            preparation_steps_is_html=False,
            is_published=True,
            cover='media/recipes/covers/2022/12/28/churrasco.jpeg'
        )
        return super().setUp()

    def test_home(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.recipe)

