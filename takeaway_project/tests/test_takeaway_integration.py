from lib.dish import *
from lib.menu import *
from lib.food_order import *
from lib.order_summary import *

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
    assert menu.all_dishes() == {"Moussaka": 12.5, "Fattoush Salad": 9.0}

"""
When adding a dish from a menu to a food order
the dish is added to an order list
"""
def test_add_dish_to_food_order():
    menu = Menu()
    moussaka = Dish("Moussaka")
    fattoush = Dish("Fattoush Salad")
    moussaka.set_price(12.5)
    fattoush.set_price(9.0)
    menu.add(moussaka)
    menu.add(fattoush)
    order = FoodOrder(menu)
    order.add("Moussaka")
    assert order._basket == {"Moussaka": 12.5}


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
    order.add("Moussaka")
    order.add("Fattoush")
    order.remove("Moussaka")
    assert order._basket == {"Fattoush": 9.0}

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
    order.add("Moussaka")
    order.add("Fattoush")
    order.add("Malabi")
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
    order.add("Moussaka")
    order.add("Fattoush")
    order_summary = OrderSummary(order)
    assert order_summary.view() == ([("Moussaka", 12.5), ("Fattoush", 9.0)], ("Total", 21.5))

"""
When viewing a summary where there's two of the same item
that item appears twice with its original price
e.g Salad price is 5,  
{salad: 10} means two salads have been added to order
in summary we should see [(salad, 5), (salad, 5)]
"""
def test_view_lists_identical_items_seperately():
    menu = Menu()
    moussaka = Dish("Moussaka")
    hummus = Dish("Hummus")
    moussaka.set_price(12.5)
    hummus.set_price(5.0)
    menu.add(moussaka)
    menu.add(hummus)
    order = FoodOrder(menu)
    order.add("Moussaka")
    order.add("Moussaka")
    order.add("Hummus")
    order_summary = OrderSummary(order)
    assert order_summary.view() == ([("Moussaka", 12.5), ("Moussaka", 12.5), ("Hummus", 5)], ("Total" ,30))