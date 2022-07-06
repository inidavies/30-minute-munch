import requests
import pandas as pd
import sqlalchemy as db

API_KEY = "ceeb271bddmshe389392044c13efp170620jsn7cfdf68bc735"
API_HOST = "tasty.p.rapidapi.com"

#Prompts the user to enter a valid ingredient (strings only) and returns that ingredient
def get_user_ingredient():
    ingredient = input('What ingredient do you want to see 30-minute recipes for?: ')
    try:
        while float(ingredient):
            ingredient = input('Not a valid ingredient. Please try again: ')
    except ValueError as e:
        pass
    return ingredient

#This should return a dictionary of recipes
def get_recipes(app_key, app_host, ingredient):
    url = "https://tasty.p.rapidapi.com/recipes/list"

    querystring = {"from":"0","size":"100","tags":"under_30_minutes", "q": ingredient}

    headers = {
        "X-RapidAPI-Key": app_key,
        "X-RapidAPI-Host": app_host
    }
    response = requests.get(url, headers=headers, params=querystring)
    return response.json()["results"]

def create_recipe_db():
    recipe_list = get_recipes(API_KEY, API_HOST, get_user_ingredient())

    # Create a dataframe for the page posts
    col_names = ["Title", "Prep-Time", "Cook-Time", "Total-Time", "Link"]
    munchies = pd.DataFrame(columns = col_names)

    for recipe in recipe_list:
        # Put the data from the post in the pandas dataframe
        #munchies.loc[len(munchies.index)] = [recipe["name"], "NULL", "NULL", "NULL", "NULL]"]
        if "prep_time_minutes" in recipe and "cook_time_minutes" in recipe and "total_time_minutes" in recipe and "video_url" in recipe:
            munchies.loc[len(munchies.index)] = [recipe["name"], recipe["prep_time_minutes"], recipe["cook_time_minutes"],recipe["total_time_minutes"], recipe["video_url"]]
    
    # Create an engine object
    engine = db.create_engine('sqlite:///30_min_munchies.db')

>>>>>>> b7c154f2c79b3d730a941670eee796b41b3a9ae6
    # Create and send sql table from your dataframe
    munchies.to_sql('recipes', con=engine, if_exists='replace', index=False)
    
    #Return Database Query
    return engine.execute("SELECT * FROM recipes;").fetchall()

def display_recipe_db():
    print("Generating Database...")
    # Create an engine object
    engine = db.create_engine('sqlite:///30_min_munchies.db')

    # Make a query and print out the database
    query_result = engine.execute("SELECT * FROM recipes;").fetchall()
    print(pd.DataFrame(query_result))

create_recipe_db()
display_recipe_db()
