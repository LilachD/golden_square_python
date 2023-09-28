class Dish():
    # User-facing: 
        # name of dish         
        # price of dish

    def __init__(self, name):
        self._name = name
        self._price = None

    def set_price(self, price):
        self._price = float(price)
