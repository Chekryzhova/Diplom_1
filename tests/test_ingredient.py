import ingredient_types
from practikum.ingredient import Ingredient
import data

class TestIngredient:

    def test_get_type_ingredient(self):
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_FILLING, data.INGREDIENT_NAME[3], data.PRICE[3])
        assert ingredient.get_type() == ingredient_types.INGREDIENT_TYPE_FILLING

    def test_get_name_ingredient(self):
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_FILLING, data.INGREDIENT_NAME[4], data.PRICE[4])
        assert ingredient.get_name() == data.INGREDIENT_NAME[4]

    def test_get_price_ingredient(self):
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_SAUCE, data.INGREDIENT_NAME[5], data.PRICE[5])
        assert ingredient.get_price() == data.PRICE[5]
