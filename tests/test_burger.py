from practikum.burger import Burger
from conftest import mock_buns, mock_ingredients
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