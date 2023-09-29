from lib.menu import *
from unittest.mock import Mock

"""
When adding a dish to a menu
menu stores it in a list
"""
def test_adding_dish_to_menu_mock():
    menu = Menu()
    dish = Mock()
    menu.add(dish)
    assert menu._all_dishes == [dish]

"""
When calling add for a dish 
that's already in menu
we get an error message
"""
def test_add_duplicate_returns_error_mock():
    menu = Menu()
    dish = Mock()
    dish._name = "Dish"
    menu.add(dish)
    assert menu.add(dish) == "Dish has already been added to the menu"

"""
when caling remove 
on a dish that's not in menu
we get None
"""
def test_removing_nonexistant_dish_returns_None_mock():
    menu = Menu()
    dish = Mock()
    assert menu.remove(dish) == None

"""
when calling remove on a dish in menu
dish is removed from the list
"""
def test_remove_removes_item_mock():
    menu = Menu()
    dish = Mock()
    dish2 = Mock()
    menu.add(dish)
    menu.add(dish2)
    menu.remove(dish2)
    assert menu._all_dishes == [dish]

"""
When adding two dishes to a menu
show_all returns a string 
with all dishes and their prices
"""
def test_show_all_lists_dishes_with_prices_mock():
    menu = Menu()
    moussaka = Mock()
    fattoush = Mock()
    moussaka.format.return_value = "Moussaka  £12.5"
    fattoush.format.return_value = "Fattoush  £9.0"
    menu.add(moussaka)
    menu.add(fattoush)
    assert menu.show_all() == "Moussaka  £12.5\nFattoush  £9.0"