from unittest.mock import Mock
from lib.order_summary import *

"""
When instantiating OrderSummary with a food order,
sum_up returns the total price of all items in order
"""
def test_order_summary_sum_up_adds_up_all_prices():
    order = Mock()
    order._basket.values.return_value = [3.5, 4.0]
    order_summary = OrderSummary(order)
    assert order_summary.sum_up() == 7.5

"""
When viewing a summary where there's two of the same item
that item appears twice with its original price
e.g Salad price is 5,  
{salad: 10} means two salads have been added to order
in summary we should see [(salad, 5), (salad, 5)]
"""
# def test_view_lists_identical_items_seperately_mock():
    # order = Mock()
    # order._basket = {"Hummus": 11, "Chips": 12}
    # order._menu = {"Hummus": 5.5, "Chips": 4}
    # order._basket.keys.return_value = ["Hummus", "Chips"]
    # order_summary = OrderSummary(order)
    # assert order_summary.view() == ([("Hummus", 5.5), ("Hummus", 5.5), ("Chips", 4), ("Chips", 4), ("Chips", 4)], ("Total" ,23))