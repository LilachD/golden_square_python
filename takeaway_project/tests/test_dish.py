from lib.dish import *

"""
when calling set_price with 2.6
the price propery is set to 2.6
"""
def test_setting_price():
    dish = Dish("name")
    dish.set_price(3.4)
    assert dish._price == 3.4

"""
When calling set_price on a priced dish 
the new price overrides the previous
"""
def test_set_new_price():
    dish = Dish("name")
    dish.set_price(3.4)
    dish.set_price(4.5)
    assert dish._price == 4.5

"""
when calling set price with integer 
dish._price is set as a float
"""
def test_set_price_as_float():
    dish = Dish("name")
    dish.set_price(3)
    assert dish._price == 3.0
