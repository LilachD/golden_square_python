class FoodOrder():

    def __init__(self, menu):
        self._menu = menu.all_dishes()
        self._basket = {}
            # sets variable to check if order has been submitted
        pass 

    def add(self, dish_name):
        if dish_name in self._basket:
            self._basket[dish_name] += self._menu[dish_name]
        else:
            self._basket[dish_name] = self._menu[dish_name]

    def remove(self, dish_name):
        if self._basket[dish_name] != self._menu[dish_name]:
            self._basket[dish_name] -= self._menu[dish_name]
        else:    
            del self._basket[dish_name]
    
    def show_basket(self):
        return self._basket

    
