import pandas as pd
import re
import convert_to_md
import creating_and_formatting_dataframe as df_creation

#get the dataframe
recipes = df_creation.dataframe_creation()

with open('md_template.txt','r') as file:
    template = file.read()

convert_to_md.get_all_recipe_labels(recipes)

#for each recipe
for i in range(0,len(recipes)):

    infos = dict(recipes.loc[i,:])
    completed_recipe = convert_to_md.create_md_recipe(infos,template)
    convert_to_md.write_md_file(completed_recipe,infos['recipeName'])
