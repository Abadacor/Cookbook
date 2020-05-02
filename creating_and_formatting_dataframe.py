import pandas as pd
import googleAPI as api

def dataframe_creation():
    #This part is for getting the CSV and making it into a dataframe
    recipes = api.get_recipes_dataframe()

    #Any techincal error in the csv that might have happened and is not a valid recipe will likely not have a name
    #so we drop any row with no recipe name
    recipes.dropna(subset=['recipeName'], inplace=True)

    #We do not need that column to work
    recipes = recipes.drop(columns=['Horodateur'])

    return recipes
