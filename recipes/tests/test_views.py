
from django.urls import resolve, reverse

from recipes import views
from recipes.tests.test_base import Recipe_test_base

# Create your tests here.


class Recipeviews(Recipe_test_base):

    def test_cate(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.category)

    def test_id(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(view.func, views.recipes)

    def test_recipe_home_view_returns_status_code_200_OK(self):
        aux = reverse('recipes:home')
        response = self.client.get(aux)
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

    def test_recipe_home_com_receitas_n_publicadas(self):
        self.make_recipe(title='aaa', is_published=False)
        response = self.client.get(reverse('recipes:home'))

        self.assertIn(
            'sem  receitas',
            response.content.decode('utf-8')
        )

    def test_recipe_home_com_receitas(self):
        self.make_recipe(title='aaa')
        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')
        self.assertIn('aaa', content)

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

    def test_recipe_category_view_returns_status_code_404(self):
        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 100}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_view_returns_status_code_404(self):

        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_search_404_if_no_search(self):
        self.assertEqual(1, 1)

    def test_recipe_search_uses_correct_view_function(self):
        resolved = resolve(reverse('recipes:search'))
        self.assertIs(resolved.func, views.search)
