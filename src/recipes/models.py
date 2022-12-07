from django.db import models

# Create your models here.
class Recipe(models.Model):
  name = models.CharField(max_length=120)
  category_choices = (
    ('starter',
    'Starter'),
    ('main',
    'Main'),
    ('dessert',
    'Dessert')
    )

  category = models.CharField(max_length=12, choices=category_choices, default='main')

  preparation_time = models.PositiveIntegerField(help_text= 'in minutes')

  cooking_time = models.PositiveIntegerField(help_text= 'in minutes')

  serving = models.PositiveIntegerField()

  difficulty_choices = (('easy','Easy'),('medium','Medium'),('intermediate','Intermediate'), ('hard','Hard'))

  difficulty = models.CharField(max_length=12, choices=difficulty_choices, default='intermediate')

  ingredients = models.CharField(max_length=240)

  directions = models.CharField(max_length=240)

  notes = models.CharField(max_length=240)

  def __str__(self):
    return str(self.name)