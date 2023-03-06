
from django.urls import resolve, reverse

from recipes import views
from recipes.tests.test_base import Recipe_test_base

# Create your tests here.


class RecipeCateviews(Recipe_test_base):
    def test_recipe_cate_com_receitas(self):
        self.make_recipe(title='aaa')
        response = self.client.get(reverse('recipes:category', args=(1,)))
        content = response.content.decode('utf-8')
        self.assertIn('aaa', content)

    def test_recipe_cate_com_receitas_n_publicadas(self):
        recipe = self.make_recipe(title='aaa', is_published=False)
        response = self.client.get(
            reverse('recipes:category', args=(recipe.id,)))

        self.assertEqual(response.status_code, 404)

    def test_cate(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.category)

    def test_recipe_category_view_returns_status_code_404(self):
        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 100}))
        self.assertEqual(response.status_code, 404)
