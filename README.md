##### 30 minute Munch
###### By: Ini Davies, T'airra Champliss

# Requirements

_Python 3_

### _Libraries_: requests, pandas, SQLAlchemy
### _API used_: [Tasty](https://rapidapi.com/apidojo/api/tasty/)
### _Testing Modules_: unittest

# Understanding of code:
An explanation of the functions:
- ```get_user_ingredient()```: Prompts the user for an ingredient that they would like to see 30 minute recipes for; the prompt does not accept integers or floats, only strings. Returns: The user's ingredient.
- ```get_recipes(app_key, app_host, ingredient)```: Generates a connection to the Tasty API. Returns: A database of the API.
- ```create_recipe_db(ingredient)```: Utilizes the user's ingredient to filter through the database, select recipes with that ingredient, and store in a data frame. Returns: A filtered data frame.
- ```recipe_choice(index_list)```: Prompts the user for the index for the recipe they want to see more info about; the prompt only accepts indices between 1 and the total number of recipes displayed (no strings or unreachable indexes). Returns: The user's recipe index.
- ```display_recipe_db(query_result, ingredient)```: Formats the data frame to be user-friendly and user-readable. Returns: A list of recipes with the ingredients, which includes the recipe name, prep time, cook time, total time, and a how-to video link.

# How to setup and run:
Before running the program, please make sure you have the requests, SQLAlchemy, and pandas packages installed on your machine.
Please also note that the Tasty API does not require authentication from the user, so setup for that is not required.
Download a zip file of our code i(nto a folder that you can locate later) and upzip it. You can run the program from your computer terminal, a python IDLE, or a source-code editor (such as Visual Studio Code). If you want run the program with the python command, you need to open a command-line and enter the following:

> python3 30-min-munch

Please note: You must be in the directory that the file is in to run it. Another alternative to this command is to replace the file name with the file path.

# How to watch video included:
Press the link provided with the recipe you want to follow. The video should automatically download onto your device. The videos are provided directly from the API with file extensions .m3u8. These file types can be played on Windows Media Player, but may require other programs (Videolan VLC media player, Songbird). Please see this [link](https://fileinfo.com/extension/m3u8#:~:text=How%20to%20open%20an%20M3U8%20file&text=You%20can%20open%20an%20M3U8,VLC%20media%20player%20(multiplatform).) for more info.

# Sample Execution and Output:
```
Welcome to 30 minute munch!
Enter an ingredient and we will give you a list of recipes
All our recipes take 30 minutes or less to make!
Let's get started!

[Prompt] Enter an ingredient: 'cucumber'

Here are your 30 minute cucumber  recipes...

1   Tasty’s Purple Goddess 
Total Time: 15 minutes


2   Falafel Waffle 
Total Time: 30 minutes


3   Vietnamese Lemongrass BBQ Pork (Thịt Nướng) As Made By Omsom 
Total Time: 15 minutes


4   Collard Salad With Warm Bacon Dressing As Made By Alex Hill 
Total Time: 25 minutes


5   Vegan Spring Roll In A Bowl 
Total Time: 22 minutes


6   Goat Cheese And Cucumber Crostini 
Total Time: 30 minutes


Which recipe would you like to try?

[Prompt] Choose a recipe index: '2'

Recipe: Falafel Waffle
Prep Time: 20 minutes
Cook Time: 10 minutes
Total Time: 30 minutes
Video:  None
Description: This recipe is a perfect Mediterranean appetizer, vegetarian snack or savory breakfast! Fill your Falafel Waffle with your favorite toppings like hummus, tahini, feta, vegetables or meat. Try making your own Falafel Waffle Sandwich for breakfast, lunch or dinner. This easy snack is definitely a must try.
Instructions: 
       1. To the bowl of a 2-quart (2 liter) food processor, add the chickpeas, onion, parsley, garlic, lemon juice, and spices. Pulse the ingredients together until just incorporated and they form a wet paste. Be careful not to overblend.
       2. Transfer the chickpea mixture to a large bowl and add the bread crumbs, mixing until just incorporated. Cover with plastic wrap and refrigerate for 1-2 hours, or overnight.
       3. Remove the chilled falafel mixture from the refrigerator and shape into 1-inch balls. The mixture should yield 18-20 balls.
       4. Preheat waffle iron and brush with olive oil. Place one falafel ball onto iron and cook for 5 minutes.
       5. Serve as desired with your favorite toppings or as a sandwich.
       6. Enjoy!
```
