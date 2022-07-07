import unittest
from 3-min-munch import get_user_filter, get_recipes, create_recipe_db, display_recipe_db


class Unit_test(unittest.TestCase):
    def test_get_user_ingredient(self):
        self.assertEqual(get_user_ingredient(), None)

    # To be added once main code works
    '''def test_get_restrictions(self):
        self.assertEqual(get_restrictions(), None)'''

    def test_get_recipes(self):
        self.assertEqual(get_recipes(), None)

    def test_create_recipe_db(self):
        self.assertEqual(create_recipe_db(), None)

    def test_display_recipe_db(self):
        self.assertEqual(display_recipe_db(), None)


if __name__ == '__main__':
    unittest.main()
