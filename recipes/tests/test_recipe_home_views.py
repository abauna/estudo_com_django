from django.urls import reverse

from recipes.tests.test_base import Recipe_test_base

# Create your tests here.


class RecipeHomeviews(Recipe_test_base):

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
