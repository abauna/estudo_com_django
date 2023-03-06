
from django.urls import resolve, reverse

from recipes import views
from recipes.tests.test_base import Recipe_test_base

# Create your tests here.


class Recipeviews(Recipe_test_base):

    def test_id(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(view.func, views.recipes)

    def test_recipe_view_returns_status_code_404(self):

        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertEqual(response.status_code, 404)
