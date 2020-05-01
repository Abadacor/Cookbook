import unidecode

#This function is used to create a .tex file from information contained in ',' separated row of recipes spreadsheet
# @param: infos -- row information of a dataframe (probably gotten from index cause i'm too lazy to do it properly)
# @param: recipe -- *.tex template file for a recipe. Information to be replaced is identified like so: [field_id]
def create_latex_recipe(infos, recipe):

    #Format the ingredients list from the information into lists items for LateX
    ingList = list(infos['ingredients'].strip().split('. '))
    for j in range(len(ingList)):
        if(j > 0):
            ingList[j] = "\t    \item " + ingList[j] + "\n"
        else:
            ingList[j] = "\item " + ingList[j] + "\n"
    infos['ingredients'] = "".join(ingList)

    #Same operation for the preparation instructions
    prepList = list(infos['preparation'].strip().split('. '))
    for j in range(len(prepList)):
        if(j > 0):
            prepList[j] = "\t    \item " + prepList[j] + "\n"
        else:
            prepList[j] = "\item " + prepList[j] + "\n"
    infos['preparation'] = "".join(prepList)

    #Then replace the identifiers with the right information within the template (some of them need some existence checking)
    recipe = recipe.replace('[recipeName]',infos['recipeName'])
    recipe = recipe.replace('[prepTime]',infos['prepTime'])
    recipe = recipe.replace('[difficulty]',str(infos['difficulty']))
    if(type(infos['advice']) is not float):
            recipe = recipe.replace('[advice]',"\subsection{Trucs \& Astuces}\n\t" + infos['advice'])
    else:
            recipe = recipe.replace('[advice]',"")
    recipe = recipe.replace('[nbOfPeople]',str(infos['nbOfPeople']))
    recipe = recipe.replace('[ingredients]',str(infos['ingredients']))
    recipe = recipe.replace('[preparation]',str(infos['preparation']))

    if(type(infos['quote']) is not float):
        recipe = recipe.replace('[Quote]',"\begin{chapquote}{[quoteAuthor], \textit{[quoteAuthorText]}}\n\`\`" + str(infos['quote'] + "\n\'\'\n\end{chapquote}\n"))
        recipe = recipe.replace('[quoteAuthor]',str(infos['quoteAuthor']))
        recipe = recipe.replace('[quoteAuthorText]',str(infos['quoteAuthorText']))

    print("Recipe created")
    return recipe

def write_tex_file(recipe, recipeName):
    with open("texRecipes/" + unidecode.unidecode(recipeName.replace(" ",""))+'.tex','w') as file:
        file.write(recipe)
        print("file written to file!")

def get_recipe_label(recipeInfo):
    return '\item \hyperref[sec:'+recipeInfo['recipeName']+']{'+recipeInfo['recipeName']+'}\n'

def get_all_recipe_labels(recipes):
    with open('names.txt','a') as file:
        for i in range(1,len(recipes)):
            infos = recipes.loc[i,:]
            file.write(get_recipe_label(infos))
