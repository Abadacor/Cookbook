import googleAPI as api
import creating_and_formatting_dataframe as df_creation
import sys

#information for the command line function
usage = "To use this command:\n \
        python3 add_recipe.py -h or python3 add_recipe.py --help to see this message\n \
        Mandatory arguments are:\n \
        --name recipe_name\n \
        --prepTime \"<= time_in_minutes\"\n \
        --difficulty number_on_1to5_scale \n \
        --nbOfPeople number\n \
        --ingredients \"period.separated.ingredients.\"\n \
        --preparation \"period.separated.preparation.steps.\"\n \
        Optional arguments are:\n \
        --category [entrée|plat|dessert]\n \
        --quote \"quote\"\n \
        --quoteAuthor \"author name\"\n \
        --quoteAuthorText\"added text to give author context\"\n \
        --advice \"advice\"\n \
        "
errorMessage = "Incorrect command, you probably don't have all the required arguments, please use -h or --help to see help. Fucker."


#row creation function
def create_row(args):
    print(args)

#getting the current recipes
recipes = api.get_recipes_dataframe()

#create a dictionnary from the arguments with key = column names and values = args
args = sys.argv
if(len(sys.argv) >= 2):
    if(sys.argv[1] == "-h" or sys.argv[1] == "--help"):
        print(usage)
#    elif(len(sys.argv)>=13):
    elif("--name" in args and \
            "--prepTime" in args and \
            "--difficulty" in args and \
            "--nbOfPeople" in args and \
            "--ingredients" in args and \
            "--preparation" in args):
        create_row(sys.argv)
    else:
        print(errorMessage)
else:
    print(usage)
