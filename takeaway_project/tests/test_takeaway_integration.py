from lib.dish import *
from lib.menu import *
from lib.food_order import *
from lib.order_summary import *
from lib.text_confirmation import *

"""
When adding a dish to a menu
menu stores it in a dictionary
"""
def test_adding_dish_to_menu():
    menu = Menu()
    dish = Dish("name")
    menu.add(dish)
    assert menu._all_dishes == [dish]

"""
When adding two dishes to a menu
we can see a list of all dishes and their prices
"""
def test_show_all_lists_dishes_with_prices():
    menu = Menu()
    moussaka = Dish("Moussaka")
    fattoush = Dish("Fattoush Salad")
    moussaka.set_price(12.5)
    fattoush.set_price(9)
    menu.add(moussaka)
    menu.add(fattoush)
    assert menu.show_all() == "Moussaka  £12.5\nFattoush Salad  £9.0"

"""
When adding a dish that isn't in menu 
food_order.add() returns error message
"""
def test_add_unavailable_dish_to_food_order_returns_error():
    menu = Menu()
    moussaka = Dish("Moussaka")
    fattoush = Dish("Fattoush Salad")
    moussaka.set_price(12.5)
    fattoush.set_price(9.0)
    menu.add(moussaka)
    order = FoodOrder(menu)
    assert order.add(fattoush) == "Fattoush Salad is not available to order at the moment"


"""
When removing a dish from food order
the dish is removed from the order list
"""
def test_remove_dish_from_food_order():
    menu = Menu()
    moussaka = Dish("Moussaka")
    fattoush = Dish("Fattoush")
    moussaka.set_price(12.5)
    fattoush.set_price(9.0)
    menu.add(moussaka)
    menu.add(fattoush)
    order = FoodOrder(menu)
    order.add(moussaka)
    order.add(fattoush)
    order.remove(moussaka)
    assert order._basket == [fattoush]

"""
When instantiating OrderSummary with a food order,
sum_up returns the total price of all items in order
"""
def test_order_summary_sum_up_adds_up_all_prices():
    menu = Menu()
    moussaka = Dish("Moussaka")
    fattoush = Dish("Fattoush")
    malabi = Dish("Malabi")
    moussaka.set_price(12.5)
    fattoush.set_price(9.0)
    malabi.set_price(6.5)
    menu.add(moussaka)
    menu.add(fattoush)
    menu.add(malabi)
    order = FoodOrder(menu)
    order.add(moussaka)
    order.add(fattoush)
    order.add(malabi)
    order_summary = OrderSummary(order)
    assert order_summary.sum_up() == 28.0


"""
When viewing a food order with two menu dishes in it
We get a list of two dishes with prices and grand total 
"""
def test_order_summary_view_returns_itemised_list_with_total():
    menu = Menu()
    moussaka = Dish("Moussaka")
    fattoush = Dish("Fattoush")
    moussaka.set_price(12.5)
    fattoush.set_price(9.0)
    menu.add(moussaka)
    menu.add(fattoush)
    order = FoodOrder(menu)
    order.add(moussaka)
    order.add(fattoush)
    order_summary = OrderSummary(order)
    assert order_summary.view() == "Moussaka  £12.5\nFattoush  £9.0\n Total: £21.5"

