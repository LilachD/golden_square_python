class FoodOrder():
    def __init__(self, menu):
        self._menu = menu._all_dishes
        self._basket = []
            # sets variable to check if order has been submitted
        pass 

    def add(self, dish):
        if dish not in self._menu:
            return f"{dish._name} is not available to order at the moment"
        else:
            self._basket.append(dish)

    def remove(self, dish):
        if dish in self._basket:
            self._basket.remove(dish)
                
    
    def show_basket(self):
        return self._basket

    
