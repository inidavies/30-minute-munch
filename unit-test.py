import unittest
from unittest.mock import patch
from 30-min-munch import get_user_ingredient, get_recipes, create_recipe_db, display_recipe_db
config {
    API_KEY = "ceeb271bddmshe389392044c13efp170620jsn7cfdf68bc735"
    API_HOST = "tasty.p.rapidapi.com"
}
class Unit_test(unittest.TestCase):
    # Create a mock object for the user input
    @patch('builtins.input', return='rice')
    def test_get_user_ingredient(self, mock_input):
        input_test = get_user_ingredient
        self.assertEqual(input_test, 'rice')
    
    # To be added once main code works
    '''def test_get_restrictions(self):
        self.assertEqual(get_restrictions(), None)'''
    
    # Tests for a successful connection to the API data
    def test_get_recipes(self):
        url = "https://tasty.p.rapidapi.com/recipes/list"
        resp = requests.get(url)
        self.assertEqual(get_recipes(API_KEY, API_HOST, ''), resp)
    
    # Tests for the validity of the database query
    def test_create_recipe_db(self):
        self.assertEqual(create_recipe_db().json(), )
    
    # The display is formatted correctly and returns the correct output
    def test_display_recipe_db(self):
        self.assertEqual(display_recipe_db(), None)
if __name__ == '__main__':
    unittest.main()