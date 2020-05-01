import pandas as pd
import re
import convert_to_latex
import googleAPI as api

#This part is for getting the CSV and making it into a dataframe
#recipes = pd.read_csv('recipes.csv')
recipes = api.get_recipes_dataframe()
recipes = recipes.drop(recipes.index[0:1])
recipes = recipes.drop(columns=['timestamps'])


with open('template.txt','r') as file:
    template = file.read()

#for each recipe
for i in range(1,len(recipes)):

    infos = recipes.loc[i,:]
    completed_recipe = convert_to_latex.create_latex_recipe(infos,template)
    convert_to_latex.write_tex_file(completed_recipe,infos['recipeName'])
