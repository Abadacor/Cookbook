import pandas as pd
import re
import convert_to_latex
import creating_and_formatting_dataframe as df_creation

#get the dataframe
recipes = df_creation.dataframe_creation()

with open('template.txt','r') as file:
    template = file.read()

#for each recipe
for i in range(0,len(recipes)):

    infos = dict(recipes.loc[i,:])
    completed_recipe = convert_to_latex.create_latex_recipe(infos,template)
    convert_to_latex.write_tex_file(completed_recipe,infos['recipeName'])
