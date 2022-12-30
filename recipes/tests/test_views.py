from django.test import TestCase
from django.urls import resolve, reverse

from recipes import views

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

    def test_recipe_category_view_returns_status_code_404(self):
        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 100}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_view_returns_status_code_404(self):
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertEqual(response.status_code, 404)
