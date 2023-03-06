from django.urls import resolve, reverse

from recipes import views
from recipes.tests.test_base import Recipe_test_base

# Create your tests here.


class RecipeSearchviews(Recipe_test_base):

    def test_recipe_search_404_if_no_search(self):
        self.assertEqual(1, 1)

    def test_recipe_search_uses_correct_view_function(self):
        resolved = resolve(reverse('recipes:search'))
        self.assertIs(resolved.func, views.search)

    def test_recipe_search_loads_correct_template(self):
        response = self.client.get(reverse('recipes:search') + '?q=teste')
        self.assertTemplateUsed(response, 'page/search.html')

    def test_recipe_search_raises_404_no_term(self):
        response = self.client.get(reverse('recipes:search'))
        self.assertEqual(response.status_code, 404)

    def test_search_term_escapa_e_tem_titulo(self):
        response = self.client.get(reverse('recipes:search') + '?q=teste')
        self.assertIn('Search for &quot;teste&quot;',
                      response.content.decode('utf-8'))
