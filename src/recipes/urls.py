from django.urls import path
from .views import recipes_home, RecipeListView, RecipeDetailView

app_name = 'recipes_home'

urlpatterns = [
  path('', recipes_home),
  path('list/', RecipeListView.as_view(), name='list'),
  path('list/<pk>', RecipeDetailView.as_view(), name='detail'),
]