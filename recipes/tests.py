from django.test import TestCase
from .models import Recipe  #to access Recipe model

from .forms import RecipesSearchForm

# Create your tests here.
class RecipeModelTest(TestCase):

  def setUpTestData():
    # Set up non-modified objects used by all test methods
    Recipe.objects.create(name='Cake', category='dessert', preparation_time='15', cooking_time='35', serving='6', difficulty='medium', ingredients='Flour, Milk, Yeast, Egg', directions='Put everything together', notes='Notes go here...')

  def test_recipe_name(self):
    # Get a recipe object to test
    recipe = Recipe.objects.get(id=1)

    # Get the metadata for the 'name' field and use it to query its data
    field_label = recipe._meta.get_field('name').verbose_name

    # Compare the value to the expected result
    self.assertEqual(field_label, 'name')

  def test_name_max_length(self):
    # Get a recipe object to test
    recipe = Recipe.objects.get(id=1)

    # Get the metadata for the 'name' field and use it to query its max_length
    max_length = recipe._meta.get_field('name').max_length

    # Compare the value to the expected result i.e. 120
    self.assertEqual(max_length, 120)

  def test_ingredients_max_length(self):
    # Get a recipe object to test
    recipe = Recipe.objects.get(id=1)

    # Get the metadata for the 'ingredients' field and use it to query its max_length
    max_length = recipe._meta.get_field('ingredients').max_length

    # Compare the value to the expected result i.e. 240
    self.assertEqual(max_length, 240)

  def test_directions_max_length(self):
    # Get a recipe object to test
    recipe = Recipe.objects.get(id=1)

    # Get the metadata for the 'directions' field and use it to query its max_length
    max_length = recipe._meta.get_field('directions').max_length

    # Compare the value to the expected result i.e. 240
    self.assertEqual(max_length, 240)


  def test_notes_max_length(self):
    # Get a recipe object to test
    recipe = Recipe.objects.get(id=1)

    # Get the metadata for the 'notes' field and use it to query its max_length
    max_length = recipe._meta.get_field('notes').max_length

    # Compare the value to the expected result i.e. 240
    self.assertEqual(max_length, 240)


  def test_get_absolute_url(self):
    recipe = Recipe.objects.get(id=1)
    #get_absolute_url() should take you to the detail page of recipe #1
    #and load the URL /recipes/list/1
    self.assertEqual(recipe.get_absolute_url(), '/recipes/list/1')

  def test_form_validation_with_valid_data(self):
    form = RecipesSearchForm({'recipe_category': 'dessert', 'chart_type': '#1'})
    self.assertTrue(form.is_valid())
