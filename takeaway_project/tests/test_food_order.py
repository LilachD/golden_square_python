from unittest.mock import Mock
from lib.food_order import *

"""
When adding a dish that isn't in menu 
food_order.add() returns error message
"""
def test_add_dish_not_in_menu_returns_error_mock():
    menu = Mock()
    menu._all_dishes = []
    item = Mock()
    item._name = "item"
    order = FoodOrder(menu)
    assert order.add(item) == "item is not available to order at the moment"

"""
when calling add for an item in menu
the item is added to basket
"""
def test_adding_an_item_to_basket_mock():
    menu = Mock()
    item = Mock()
    menu._all_dishes = [item]
    order = FoodOrder(menu)
    order.add(item)
    assert order._basket == [item]

"""
when calling remove with an item
that has been added twice
only one occurance is removed
"""
def test_removes_only_one_item_mock():
    menu = Mock()
    item = Mock()
    item2 = Mock()
    menu._all_dishes = [item2, item, item]
    order = FoodOrder(menu)
    order.remove(item) 
    order.show_basket() == [item2, item]



