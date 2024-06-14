from practikum.burger import Burger
from conftest import mock_buns, mock_ingredients, mock_second_ingredients
import data


class TestBurger:

    def test_set_buns(self, mock_buns):
        burger = Burger()
        burger.set_buns(mock_buns)

        assert burger.bun == mock_buns

    def test_add_ingredient(self, mock_ingredients):
        burger = Burger()
        burger.add_ingredient(mock_ingredients)

        assert burger.ingredients == [mock_ingredients]

    def test_get_price(self, mock_buns, mock_ingredients):
        burger = Burger()
        burger.bun = mock_buns
        burger.ingredients = [mock_ingredients]

        assert burger.get_price() == data.PRICE_BURGER

    def test_remove_ingredient(self, mock_ingredients):
        burger = Burger()
        burger.add_ingredient(mock_ingredients)
        burger.remove_ingredient(0)

        assert burger.ingredients == []

    def test_move_ingredient(self, mock_ingredients, mock_second_ingredients):
        burger = Burger()
        burger.add_ingredient(mock_ingredients)
        burger.add_ingredient(mock_second_ingredients)
        burger.move_ingredient(1, 0)

        assert burger.ingredients[0] == mock_second_ingredients

    def test_get_receipt(self, mock_buns, mock_ingredients, mock_second_ingredients):
        burger = Burger()
        burger.set_buns(mock_buns)
        burger.add_ingredient(mock_ingredients)
        burger.add_ingredient(mock_second_ingredients)

        assert burger.get_receipt() == data.RECEIPT


