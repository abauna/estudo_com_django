from django.test import TestCase
from django.urls import resolve, reverse

from recipes import views

# Create your tests here.


class RecipeURLsTest(TestCase):
    def test_the_pytest_is_ok(self):
        home_url = reverse('recipes:home')
        self.assertEqual(home_url, '/')

    def test_url(self):
        url = reverse('recipes:category', kwargs={'category_id': 1})
        self.assertEqual(url, '/recipes/category/1/')

    def test_url_id(self):
        url = reverse('recipes:recipe', kwargs={'id': 1})
        self.assertEqual(url, '/recipes/1/')


def test_recipe_search_url_is_correct(self):
    url = reverse('recipes:search')
    self.assertEqual(url, '/recipes/search/')
