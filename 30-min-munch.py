import requests
import pandas as pd
import sqlalchemy as db
from py_edamam import Edamam

APP_ID = "39cabb81"
APP_KEY = "0b2df6d09ea0291280c42d49e6b0bd6f"

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
def get_recipes(app_id, app_key, ingredient):
    edamam_object = Edamam(recipes_appid = app_id, recipes_appkey=app_key)
    query_result = edamam_object.search_recipe(ingredient)
    return query_result["hits"]

def create_recipe_db():
    recipe_list = get_recipes(APP_ID, APP_KEY, get_user_ingredient())

    # Create a dataframe for the page posts
    col_names = ["Title", "Time", "Link"]
    munchies = pd.DataFrame(columns = col_names)

    for recipe in recipe_list:
        # Put the data from the post in the pandas dataframe
        munchies.loc[len(munchies.index)] = [recipe["recipe"]["label"], recipe["recipe"]['totalTime'], recipe["recipe"]["url"]]
    
    # Create an engine object
    engine = db.create_engine('sqlite:///30_min_munchies.db')

    # Create and send sql table from your dataframe
    munchies.to_sql('recipes', con=engine, if_exists='replace', index=False)
    
    #Return Database Query
    return engine.execute("SELECT * FROM recipes;").fetchall()
    
def display_recipe_db():
    # Create an engine object
    engine = db.create_engine('sqlite:///30_min_munchies.db')

    # Make a query and print out the database
    query_result = engine.execute("SELECT * FROM recipes;").fetchall()
    print(pd.DataFrame(query_result))


create_recipe_db()
display_recipe_db()