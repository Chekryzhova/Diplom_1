import ingredient_types
from practikum.database import Database
import pytest


class TestDatabase:

    def test_database_initialization(self):
        database = Database()

        assert len(database.buns) == 3 and len(database.ingredients) == 6

    @pytest.mark.parametrize("name, price", [
        ("black bun", 100),
        ("white bun", 200),
        ("red bun", 300)
    ])
    def test_available_buns(self, name, price):
        database = Database()
        buns_list = database.available_buns()
        assert any(bun.name == name and bun.price == price for bun in buns_list)

    @pytest.mark.parametrize("type, name, price", [
        (ingredient_types.INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (ingredient_types.INGREDIENT_TYPE_SAUCE, "sour cream", 200),
        (ingredient_types.INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
        (ingredient_types.INGREDIENT_TYPE_FILLING, "cutlet", 100),
        (ingredient_types.INGREDIENT_TYPE_FILLING, "dinosaur", 200),
        (ingredient_types.INGREDIENT_TYPE_FILLING, "sausage", 300)
    ])
    def test_available_ingredients(self, type, name, price):
        database = Database()
        ingredients_list = database.available_ingredients()

        assert any(ingredient.name == name and ingredient.price == price and ingredient.type == type for ingredient in ingredients_list)


