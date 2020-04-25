import pandas as pd
import re

recipes = pd.read_csv('recipes.csv')
recipes = recipes.drop(recipes.index[0:1])
recipes = recipes.drop(columns=['timestamps'])
#print(recipes)

#recipe = recipes.loc[1,:]
#print(recipe['recipeName'])

with open('template.txt','r') as file:
    template = file.read()

#for each recipe
for i in range(1,len(recipes)):
#for i in range(1,6):
    infos = recipes.loc[i,:]
    recipe = template

    ingList = list(infos['ingredients'].split('. '))
    for j in range(len(ingList)):
        if(j > 0):
            ingList[j] = "\t    \item " + ingList[j] + "\n"
        else:
            ingList[j] = "\item " + ingList[j] + "\n"
    infos['ingredients'] = "".join(ingList)
  
    prepList = list(infos['preparation'].split('. '))
    for j in range(len(prepList)):
        if(j > 0):
            prepList[j] = "\t    \item " + prepList[j] + "\n"
        else:
            prepList[j] = "\item " + prepList[j] + "\n"
    infos['preparation'] = "".join(prepList)

    recipe = recipe.replace('[recipeName]',infos['recipeName'])
    recipe = recipe.replace('[prepTime]',infos['prepTime'])
    recipe = recipe.replace('[difficulty]',str(infos['difficulty']))
    if(type(infos['advice']) is not float):
            recipe = recipe.replace('[advice]',infos['advice'])
    else:
            recipe = recipe.replace('[advice]',"")
    recipe = recipe.replace('[nbOfPeople]',str(infos['nbOfPeople']))
    recipe = recipe.replace('[ingredients]',str(infos['ingredients']))
    recipe = recipe.replace('[preparation]',str(infos['preparation']))

    if(type(infos['quote']) is not float):
        recipe = recipe.replace('[Quote]',str(infos['quote']))
        recipe = recipe.replace('[quoteAuthor]',str(infos['quoteAuthor']))
        recipe = recipe.replace('[quoteAuthorText]',str(infos['quoteAuthorText']))
    
#    with open("recipes/" + infos['recipeName'].replace(" ","")+'.tex','w') as file:
#        file.write(recipe)
    
    with open('names.txt','a') as file:
        file.write('\item \hyperref[sec:'+infos['recipeName']+']{'+infos['recipeName']+'}\n')

#    print(recipe)



