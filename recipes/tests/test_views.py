
from recipes.models import Category, Recipe
from recipes import views
from django.urls import resolve, reverse
from django.test import TestCase
from django.contrib.auth.models import User
from random import randint

from faker import Faker


def rand_ratio():
    return randint(840, 900), randint(473, 573)


fake = Faker('pt_BR')


# Create your tests here.


class Recipeviews(TestCase):
    def test_home(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.recipe)

    def test_cate(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.category)

    def test_id(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(view.func, views.recipes)

    def test_recipe_home_view_returns_status_code_200_OK(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_tempetes_OK(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'page/home.html')

    def test_recipe_home_sem_receitas(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(
            'sem  receitas',
            response.content.decode('utf-8')
        )

    def test_recipe_home_com_receitas(self):
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
        response = self.client.get(reverse('recipes:home'))
        content=response.content.decode('utf-8')
        self.assertIn('teste34',content)

    def test_recipe_category_view_returns_status_code_404(self):
        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 100}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_view_returns_status_code_404(self):
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertEqual(response.status_code, 404)
