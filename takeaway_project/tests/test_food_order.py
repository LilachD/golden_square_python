from unittest.mock import Mock
from lib.food_order import *

"""
when calling add for an item in menu
the item is added to basket
"""
def test_adding_an_item_to_basket_mock():
    menu = Mock()
    menu.all_dishes.return_value = {"item": 4.5}
    order = FoodOrder(menu)
    order.add("item")
    assert order._basket == {"item": 4.5}

"""
when adding an item that already exists in order
the item price goes up accordingly
"""
def test_add_adds_to_existing_item_price_mock():
    menu = Mock()
    menu.all_dishes.return_value = {"item": 4.5}
    order = FoodOrder(menu)
    order.add("item")
    order.add("item")
    assert order._basket == {"item": 9.0}

"""
When removing a dish from food order
the dish is removed from the order list
"""
def test_remove_dish_from_food_order_mock():
    menu = Mock()
    menu.all_dishes.return_value = {"item": 4.5}
    order = FoodOrder(menu)
    order.add("item")
    order.remove("item")
    assert order._basket == {}

"""
When removing an item that has been entered twice
calling remove reduces the item price accordingly
"""
def test_remove_adjusts_price_down_mock():    
    menu = Mock()
    menu.all_dishes.return_value = {"item": 4.5}
    order = FoodOrder(menu)
    order.add("item")
    order.add("item")
    order.remove("item")
    assert order._basket == {"item": 4.5}
