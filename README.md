30 minute Munch
By: Ini Davies, T'airra Champliss

# Requirements

*Python 3*

### Libraries: requests, pandas, SQLAlchemy
### API used: [Tasty](https://rapidapi.com/apidojo/api/tasty/)
### Testing Modules: unittest

### To see recipe videos:
The recipe videos are provided directly from the API with file extensions .m3u8. These file types can be played on Windows Media Player, but may require other programs (). Please see this link for more info.

# Understanding of code:
An explanation of the functions:
- get_user_ingredient(): Prompts the user for an ingredient that they would like to see 30 minute recipes for; the prompt does not accept integers or floats, only strings. Returns: The user's ingredient.
- get_recipes(app_key, app_host, ingredient): Generates a connection to the Tasty API. Returns: A database of the API.
- create_recipe_db(ingredient): Utilizes the user's ingredient to filter through the database, select recipes with that ingredient, and store in a data frame. Returns: A filtered data frame.
- display_recipe_db(query_result, ingredient): Formats the data frame to be user-friendly and user-readable. Returns: A list of recipes with the ingredients, which includes the recipe name, prep time, cook time, total time, and a how-to video link.

# How to setup and run:
Before running the program, please make sure you install the requests, SQLAlchemy, and pandas packages installed on your machine.
Please also note that the Tasty API does not require authentication, so setup for that is not required.

# How to see video included:
Press the link provided with the recipe. The video should automatically download onto your device. From there, use .m3u8 file-compatible software (Windows Web Player, Songbird, VideoLAN VLC) to play the video and follow along.

# Sample Execution and Output:
Execution prompt: 'What ingredient do you want to see 30-minute recipes for?'

User Input: 'rice'

Output:

'Here are your 30 minute rice recipes..

Recipe: Instant Pot Perfect Rice
Prep Time: 5
Cook Time: 13
Total Time: 18
Video:  https://vid.tasty.co/output/209345/hls24_1626212592.m3u8

Recipe: Hearty Rice Noodle Soup
Prep Time: 10
Cook Time: 5
Total Time: 15
Video:  https://vid.tasty.co/output/143416/hls24_1567025752.m3u8

...'