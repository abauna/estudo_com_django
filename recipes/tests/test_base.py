
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import resolve, reverse

from recipes import views
from recipes.models import Category, Recipe


class Recipe_test_base(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_home(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.recipe)

    def make_category(self, name='cate'):
        return Category.objects.create(name=name)

    def make_author(
        self,
        first_name='user',
        last_name='user',
        username='user',
        password='user',
        email='user',
    ):
        return User.objects.create(first_name=first_name,
                                   last_name=last_name,
                                   username=username,
                                   password=password,
                                   email=email
                                   )

    def make_recipe(self,
                    category=None,
                    author=None,
                    title='teste34',
                    description='teste',
                    slug='teste',
                    preparation=5,
                    preparation_time_unit='teste',
                    servings=5,
                    servings_unit='teste',
                    preparation_steps='teste',
                    preparation_steps_is_html=False,
                    is_published=True,
                    cover='media/recipes/covers/2022/12/28/churrasco.jpeg'):
        if category is None:
            category = {}
        if author is None:
            author = {}
        return Recipe.objects.create(
            category=self.make_category(**category),
            author=self.make_author(**author),
            title=title,
            description=description,
            slug=slug,
            preparation=preparation,
            preparation_time_unit=preparation_time_unit,
            servings=servings,
            servings_unit=servings_unit,
            preparation_steps=preparation_steps,
            preparation_steps_is_html=preparation_steps_is_html,
            is_published=is_published,
            cover=cover
        )
