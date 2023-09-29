from unittest.mock import Mock
from lib.order_summary import *

"""
When instantiating OrderSummary with a food order,
sum_up returns the total price of all items in order
"""
def test_order_summary_sum_up_adds_up_all_prices():
    order = Mock()
    item1 = Mock()
    item1._price = 3.0
    item2 = Mock()
    item2._price = 4.5
    order.show_basket.return_value = [item1, item2]
    order_summary = OrderSummary(order)
    assert order_summary.sum_up() == 7.5

"""
calling view returns a list 
of items and prices, and a grand total
"""
def test_view_returns_itemised_list_with_total():
    order = Mock()
    item1 = Mock()
    item1._price = 3.0
    item1.format.return_value = "Olives  £3.0"
    item2 = Mock()
    item2._price = 4.5
    item2.format.return_value = "Chips  £4.5"
    order.show_basket.return_value = [item1, item2]
    order_summary = OrderSummary(order)
    assert order_summary.view() == "Olives  £3.0\nChips  £4.5\n Total: £7.5"