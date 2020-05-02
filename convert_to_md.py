import unidecode

def create_md_recipe(infos, recipe):

    #Format the ingredients list from the information into lists items for LateX
    ingList = list(infos['ingredients'].strip().split('. '))
    
    for j in range(len(ingList)):
        ingList[j] = "- " + ingList[j] + "\n"

    infos['ingredients'] = "".join(ingList)

    #Same operation for the preparation instructions
    prepList = list(infos['preparation'].strip().split('. '))
    for j in range(len(prepList)):
        prepList[j] = "1. " + prepList[j] + "\n"
    infos['preparation'] = "".join(prepList)

    #Then replace the identifiers with the right information within the template (some of them need some existence checking)
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
        recipe = recipe.replace('[quoteSection]',"`[quote] ~ [quoteAuthor], [quoteAuthorText]`")
        recipe = recipe.replace('[quote]',str(infos['quote']))
        recipe = recipe.replace('[quoteAuthor]',str(infos['quoteAuthor']))
        recipe = recipe.replace('[quoteAuthorText]',str(infos['quoteAuthorText']))
    else:
        recipe = recipe.replace('[quoteSection]',"")

    print("Recipe created: ",infos['recipeName'])
    return recipe

def write_md_file(recipe, recipeName):
    with open("mdRecipes/" + unidecode.unidecode(recipeName.replace(" ",""))+'.md','w') as file:
        file.write(recipe)

def get_recipe_label(recipeInfo):
    return "- [" + recipeInfo['recipeName'] + "](https://github.com/Abadacor/Cookbook/blob/master/mdRecipes/" + unidecode.unidecode(recipeInfo['recipeName'].replace(" ","")) + ".md)\n"

def get_all_recipe_labels(recipes):
    with open('mdRecipes/names.txt','a') as file:
        for i in range(1,len(recipes)):
            infos = recipes.loc[i,:]
            file.write(get_recipe_label(infos))
