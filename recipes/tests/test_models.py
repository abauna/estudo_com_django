from django.core.exceptions import ValidationError
from parameterized import parameterized

from recipes.models import Recipe
from recipes.tests.test_base import Recipe_test_base


class RecipesModelTest(Recipe_test_base):
    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()

    def recipe_not_defalt(self):
        recipe = Recipe(
            category=self.make_category(name='Test'),
            author=self.make_author(username='ne'),
            title='teste34',
            description='teste',
            slug='teste',
            preparation=5,
            preparation_time_unit='teste',
            servings=5,
            servings_unit='teste',
            preparation_steps='teste',


            cover='media/recipes/covers/2022/12/28/churrasco.jpeg'

        )
        recipe.full_clean()
        recipe.save()
        return recipe

    def test_recipe_title_more_65(self):
        self.recipe.title = 'a' * 180

        with self.assertRaises(ValidationError):
            self.recipe.full_clean()

    @parameterized.expand(
        [('title', 65),
         ('description', 165),
            ('preparation_time_unit', 20),
            ('servings_unit', 20),
         ])
    def test_fields_max_len(self, field, max):
        setattr(self.recipe, field, "a"*(max+2))
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()

    def test_recipe_html_false(self):
        recipe = self.recipe_not_defalt()
        self.assertFalse(recipe.preparation_steps_is_html)

    def test_recipe_publi_false(self):
        recipe = self.recipe_not_defalt()
        self.assertFalse(recipe.is_published)

    def test_recipe_represent(self):
        self.recipe.title = 'ttt'
        self.recipe.full_clean()
        self.recipe.save()
        self.assertEqual(
            str(self.recipe), 'ttt')
