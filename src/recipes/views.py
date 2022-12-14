from django.shortcuts import render

from django.views.generic import ListView, DetailView     #to display lists and details
from .models import Recipe                                #to access Recipe model

#to protect function-based views
from django.contrib.auth.decorators import login_required

#to protect class-based view
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import RecipesSearchForm

import pandas as pd

from .utils import get_recipename_from_id, get_chart

# Create your views here.
def recipes_home(request):
  return render(request, 'recipes/recipes_home.html')

class RecipeListView(LoginRequiredMixin, ListView):      #class-based “protected” view
  model = Recipe                                         #specify model
  template_name = 'recipes/main.html'                    #specify template

class RecipeDetailView(LoginRequiredMixin, DetailView): #class-based “protected” view
  model = Recipe                                        #specify model
  template_name = 'recipes/detail.html'                 #specify template

#keep protected
@login_required
def records(request):
  # #do nothing, simply display page    
  # return render(request, 'recipes/records.html')

  #create an instance of SalesSearchForm that you defined in recipes/forms.py
  form = RecipesSearchForm(request.POST or None)
  recipes_df=None   #initialize dataframe to None
  chart = None    #initialize chart to None
  #check if the button is clicked
  if request.method =='POST':
    #read recipe_title and chart_type
    # recipe_title = request.POST.get('recipe_title')
    recipe_category = request.POST.get('recipe_category')
    chart_type = request.POST.get('chart_type')

    #display in terminal
    print (recipe_category, chart_type)

    # print ('Exploring querysets:')
    # print ('Case 1: Output of Recipe.objects.all()')
    qs=Recipe.objects.values_list('id', 'name', 'category')
    print (qs)

    qs=Recipe.objects.all()
    print (qs)
    for recipe_obj in qs:
      print(recipe_obj.id, recipe_obj.name, recipe_obj.category)

    # print ('Case 2: Output of Recipe.objects.filter(recipe_name=recipe_title)')
    # qs =Recipe.objects.filter(recipe__name=recipe_title)
    # print (qs)

    print ('Case 2: Output of Recipe.objects.filter(category=recipe_category)')
    # qs =Recipe.objects.filter(name=recipe_title)
    qs =Recipe.objects.filter(category=recipe_category)
    print (qs)


    print ('Case 3: Output of qs.values')
    print (qs.values())

    print ('Case 4: Output of qs.values_list()')
    print (qs.values_list())

    print ('Case 5: Output of Sale.objects.get(id=1)')
    obj = Recipe.objects.get(id=1)
    print (obj)


    #apply filter to extract data
    # qs =Recipe.objects.filter(recipe__name=recipe_title)
    # qs = Recipe.objects.filter(name=recipe_title)
    qs = Recipe.objects.filter(category=recipe_category)
    if qs:      #if data found
      #convert the queryset values to pandas dataframe
      recipes_df=pd.DataFrame(qs.values()) 
      print("recipes_df: ", recipes_df)
      #convert the ID to Name of recipe
      # recipes_df['recipe_id']=recipes_df['recipe_id'].apply(get_recipename_from_id)
      recipes_df['id']=recipes_df['id'].apply(get_recipename_from_id)

      #call get_chart by passing chart_type from user input, recipes dataframe and labels
      chart=get_chart(chart_type, recipes_df, labels=recipes_df['ingredients'].values)

    #convert the dataframe to HTML
      recipes_df=recipes_df.to_html()


  #pack up data to be sent to template in the context dictionary
  context={
    'form': form,
    'recipes_df': recipes_df,
    'chart': chart
    }

  #load the recipes/record.html page using the data that you just prepared
  return render(request, 'recipes/records.html', context)