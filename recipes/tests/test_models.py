from django.core.exceptions import ValidationError

from recipes.tests.test_base import Recipe_test_base


class RecipesModelTest(Recipe_test_base):
    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()

    def test_recipe_title_more_65(self):
        self.recipe.title = 'a' * 180
        
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()
