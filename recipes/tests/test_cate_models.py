from django.core.exceptions import ValidationError
from parameterized import parameterized

from recipes.models import Recipe
from recipes.tests.test_base import Recipe_test_base


class recipecatemodelTest(Recipe_test_base):
    def setUp(self) -> None:
        self.cate = self.make_category(
            name='cate_teste'
        )
        return super().setUp()

    def test_cate_models_test(self):
        self.assertEqual(
            str(self.cate),
            self.cate.name
        )

    def test_cate_max_len(self):
        self.cate.name = 'a'*155
        with self.assertRaises(ValidationError):
            self.cate.full_clean()
