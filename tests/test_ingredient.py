import ingredient_types
from practikum.ingredient import Ingredient
import data

class TestIngredient:
    def test_type_of_ingredient_true(self):
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_SAUCE, data.INGREDIENT_NAME[0], data.PRICE[0])
        assert ingredient.type == ingredient_types.INGREDIENT_TYPE_SAUCE

    def test_name_of_ingredient_true(self):
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_SAUCE, data.INGREDIENT_NAME[1], data.PRICE[1])
        assert ingredient.name == data.INGREDIENT_NAME[1]

    def test_price_of_ingredient_true(self):
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_FILLING, data.INGREDIENT_NAME[2], data.PRICE[2])
        assert ingredient.price == data.PRICE[2]

    def test_get_type_ingredient(self):
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_FILLING, data.INGREDIENT_NAME[3], data.PRICE[3])
        assert ingredient.get_type() == ingredient_types.INGREDIENT_TYPE_FILLING

    def test_get_name_ingredient(self):
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_FILLING, data.INGREDIENT_NAME[4], data.PRICE[4])
        assert ingredient.get_name() == data.INGREDIENT_NAME[4]

    def test_get_price_ingredient(self):
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_SAUCE, data.INGREDIENT_NAME[5], data.PRICE[5])
        assert ingredient.get_price() == data.PRICE[5]
