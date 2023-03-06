
from django.urls import reverse

from recipes.tests.test_base import Recipe_test_base

# Create your tests here.


class RecipeDetalhesviews(Recipe_test_base):
    def test_recipe_detales_com_receitas(self):
        self.make_recipe(title='aaa')
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 1}))
        content = response.content.decode('utf-8')
        self.assertIn('aaa', content)

    def test_recipe_detalhes_com_receitas_n_publicadas(self):
        recipe = self.make_recipe(title='aaa', is_published=False)
        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': recipe.category.id}))

        self.assertEqual(response.status_code, 404)
