import gspread
from gspread_dataframe import get_as_dataframe, set_with_dataframe
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import pandas as pd

def get_recipes_dataframe():
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('cookbook-275914-0b5766703f5d.json',scope)
    client = gspread.authorize(creds)
    sheet = client.open('Recettes').sheet1

    recipes = get_as_dataframe(sheet)
    recipes.dropna(subset=['recipeName'], inplace=True)
    return recipes

def add_row_to_dataframe(row):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('cookbook-275914-0b5766703f5d.json',scope)
    client = gspread.authorize(creds)
    sheet = client.open('Recettes').sheet1
    
    existingRecipes = get_as_dataframe(sheet)
    existingRecipes.dropna(subset=['recipeName'], inplace=True)
    updatedRecipes = existingRecipes.append(row, ignore_index=True)
    set_with_dataframe(sheet, updatedRecipes)
    
