import requests
import pandas as pd
import sqlalchemy as db

API_KEY = "ceeb271bddmshe389392044c13efp170620jsn7cfdf68bc735"
API_HOST = "tasty.p.rapidapi.com"


def get_user_ingredient():
    ''' Prompts the user to enter a valid ingredient (strings only)
     and returns that ingredient '''
    print("Welcome to 30 minute munch!")
    print("Enter an ingredient and we will give you a list of recepies")
    print("All our recepies have take 30 minutes or less to make!")
    print("Let's get started!\n")

    ingredient = input("Enter an ingredient: ")
    try:
        while float(ingredient):
            ingredient = input('Not a valid ingredient. Please try again: ')
    except ValueError as e:
        pass
    return ingredient


def get_recipes(app_key, app_host, ingredient):
    ''' This should return a dictionary of recipes '''
    url = "https://tasty.p.rapidapi.com/recipes/list"

    querystring = {"from": "0", "size": "100", 
                  "tags": "under_30_minutes", "q": ingredient}

    headers = {
        "X-RapidAPI-Key": app_key,
        "X-RapidAPI-Host": app_host
    }
    response = requests.get(url, headers=headers, params=querystring)
    return response.json()["results"]


def create_recipe_db(ingredient):
    ''' Create a dataframe for the page posts '''
    recipe_list = get_recipes(API_KEY, API_HOST, ingredient)

    col_names = ["Title", "Prep-Time", "Cook-Time", "Total-Time", "Link", "Description", "Instructions"]
    munchies = pd.DataFrame(columns=col_names)

    for recipe in recipe_list:
        # Put the data from the post in the pandas dataframe
        if "prep_time_minutes" in recipe and "cook_time_minutes" in recipe and "total_time_minutes" in recipe and "video_url" in recipe and "description" in recipe and "instructions" in recipe:
            # Generate a string of instructions
            count = 0
            instruction_list = ""
            for instr in recipe["instructions"]:
                count += 1
                instr_step = "\n" + "       " + str(count) + ". " + instr["display_text"]
                instruction_list += instr_step

            munchies.loc[len(munchies.index)] = [recipe["name"], recipe["prep_time_minutes"], recipe["cook_time_minutes"], recipe["total_time_minutes"], recipe["video_url"], recipe["description"], instruction_list]

    # Create an engine object
    engine = db.create_engine('sqlite:///30_min_munchies.db')

    # Create and send sql table from your dataframe
    munchies.to_sql('recipes', con=engine, if_exists='replace', index=False)

    # Return Database Query
    return engine.execute("SELECT * FROM recipes;").fetchall()


def display_recipe_db(query_result, ingredient):
    ''' Display a the recipes and the info associated with it '''
    if query_result != []:
        print("\nHere are your 30 minute", ingredient, " recipes...\n")
        for row in query_result:
            print("Recepie:", row[0], end="\n")
            print("Prep Time:", row[1], "minutes", end="\n")
            print("Cook Time:", row[2], "minutes", end="\n")
            print("Total Time:", row[3], "minutes", end="\n")
            print("Video: ", row[4], end="\n")
            print("Description:", row[5], end="\n")
            print("Instructions:", row[6], end="\n")
            print()
    else:
        print("\nThere are no 30 minute recipes with", ingredient, ".\n")


''' Main function calls '''
ingredient = get_user_ingredient()
display_recipe_db(create_recipe_db(ingredient), ingredient)
