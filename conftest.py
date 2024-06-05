import pytest
from unittest.mock import Mock
import data


@pytest.fixture(scope='function')
def mock_buns():
    mock_bun = Mock()
    mock_bun.get_price.return_value = data.MOCK_BUN_PRICE
    mock_bun.get_name.return_value = data.MOCK_BUN_NAME

    return mock_bun

@pytest.fixture(scope='function')
def mock_ingredients():
    mock_ingredient = Mock()
    mock_ingredient.get_type.return_value = data.MOCK_INGREDIENT_TYPE
    mock_ingredient.get_name.return_value = data.MOCK_INGREDIENT_NAME
    mock_ingredient.get_price.return_value = data.MOCK_INGREDIENT_PRICE

    return mock_ingredient
