import googleAPI as api
import creating_and_formatting_dataframe as df_creation
import sys
import convert_to_md
import convert_to_latex

#TEST COMMAND:
#python3 add_recipe.py --name test --prepTime "<=30min" --difficulty 3 --nbOfPeople 5 --ingredients "a.b.c." --preparation "d.r.f.e." --category "Entrée"

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
    row = {}
    row['advice'] = ""
    row['category'] = ""
    row['quote'] = ""
    row['quoteAuthor'] = ""
    row['quoteAuthorText'] = ""
    for i in range(1,len(args),2):
        if(args[i] == "--name"):
            row['recipeName'] = args[i+1]
        elif(args[i] == "--prepTime"):
            row['prepTime'] = str(args[i+1])
        elif(args[i] == "--difficulty"):
            row['difficulty'] = int(args[i+1])
        elif(args[i] == "--nbOfPeople"):
            row['nbOfPeople'] = int(args[i+1])
        elif(args[i] == "--ingredients"):
            row['ingredients'] = str(args[i+1])
        elif(args[i] == "--preparation"):
            row['preparation'] = str(args[i+1])
        elif(args[i] == "--category"):
            row['category'] = str(args[i+1])
        elif(args[i] == "--advice"):
            row['advice'] = str(args[i+1])
        elif(args[i] == "--quote"):
            row['quote'] = str(args[i+1])
        elif(args[i] == "--quoteAuthor"):
            row['quoteAuthor'] = str(args[i+1])
        elif(args[i] == "--quoteAuthorText"):
            row['quoteAuthorText'] = str(args[i+1])
    
    return row

#create a dictionnary from the arguments with key = column names and values = args
args = sys.argv
row = create_row(args)
print("could create the row!")

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
        api.add_row_to_dataframe(row)
        print("could add the row")
    else:
        print(errorMessage)
else:
    print(usage)

if("--md" in args):
    with open('md_template.txt','r') as file:
        template = file.read()
    convert_to_md.write_md_file(convert_to_md.create_md_recipe(row,template),row['recipeName'])
    print("could create file")
elif("--tex" in args):
    with open('tex_template.txt','r') as file:
        template = file.read()
    convert_to_latex.write_tex_file(convert_to_latex.create_latex_recipe(row,template),row['recipeName'])
else:
    print("You haven't created the associated file!")
