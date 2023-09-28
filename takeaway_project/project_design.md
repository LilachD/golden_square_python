Class Design Recipe

1. The Problem
> As a customer  
> So that I can check if I want to order something  
> I would like to see a list of dishes with prices.
> 
> As a customer  
> So that I can order the meal I want  
> I would like to be able to select some number of several available dishes.
> 
> As a customer  
> So that I can verify that my order is correct  
> I would like to see an itemised receipt with a grand total.

Use the `twilio-python` package to implement this next one. You will need to use
mocks too.

> As a customer  
> So that I am reassured that my order will be delivered on time  
> I would like to receive a text such as "Thank you! Your order was placed and
> will be delivered before 18:52" after I have ordered.

2. Structure

 [OrderConfirmation] ? [FoodOrder] <-- [ReceiptGenerator]
                         /
                        V
                    [Menu]
                      |
                      V           
                    [Dish]

class FoodOrder():
    # User-facing properties: 
        # A dictionary of dishes and prices

    def __init__(self, menu):
        # menu: an instance of Menu
        # Side effects: starts an empty dictionary for storing {dish: price} pairs
        pass 

    def add(self, dish):
        # dish: a string representing the key (name) of the item to be added
        # Returns: None
        # Side-effects: adds a dish to order dictionary
        pass

    def remove(self, dish):
        # dish: a string representing the key (name) of the item to be added  
        # Returns: None
        # Side-effects: removes a dish from order dictionary
        pass

    def sum_up(self):
        # returns: a grand total of prices in order
        pass

    def review(self): 
        # Returns: a formatted list of all added dishes
        pass


class Menu():
    # User-facing: A list of dishes

    def __init__(self):
        # Side-effects: starts a list for storing instances of Dish
        pass

    def add(self, dish):
        # dish: an instance of Dish 
        # Returns: None
        # Side-effects: adds a dish to internal list
        pass

    def show_all(self):
        # Returns: a formated list of dishes with prices
        pass


class Dish():
    # User-facing: 
        # name of dish         
        # price of dish

    def __init__(self, name):
        # name: a string representing the name of the dish
        # Side-effects: sets the name property
        pass

    def set_price(self, price):
        # price: a float representing the price of the dish
        # Side-effects: sets the price property 
        pass


class ReciptGenerator():

    def __init__(self, order):
        # order: an instance of FoodOrder
        pass

    def generate_receipt(self):
        # returns: an itemised receipt with a grand total
        pass



class OrderConfirmation():

    def __init__(self, requester, timer, customer_details):
        # requester: Python library used to make request to the twilio API
        # timer: time library used to assert the time of order
        # customer_details: including a number where the text will be sent
        # Side-effects: sets order time as the current time in hh:mm

    def calculate_eta(self):
        # Returns an eta of an hour from current time

    def send(self, customer_details):
        # Side-effects: send a text confirming order

    

3. Examples:

"""
When adding a dish to a menu
menu stores it in a list
"""

"""
When adding two dishes to a menu
we can see a list of all dishes and their prices
"""

"""
When adding a dish from a menu to a food order
the dish is added to an order list
"""

"""
When removing a dish from food order
the dish is removed from the order list
"""

"""
When reviewing a food order with two menu dishes in it
We get a formated list of two dishes with prices
"""

"""
receipt generator returns 
an itemised receipt
of order with grand total
"""

    # FoodOrder unit test:

"""
When submitting a food order
the order is marked as submitted
"""

    # Menu unit test:

""" 
When a menu contains no dishes
we get a message: "No dishes available"
""" 

    
    # OrderConfirmation unit test: 

"""
When initialised, order confirmation
sets the order time as the current time in hh:mm
"""

"""
if initialised at 13:05
order confirmation calculates an ETA of 14:05
"""

"""
order confirmation sends a text confirming ETA
to a given phone number
"""



