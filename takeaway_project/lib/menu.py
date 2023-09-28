class Menu():
    # User-facing: A list of dishes

    def __init__(self):
        self._all_dishes = []

    def add(self, dish):
        self._all_dishes.append(dish)

    def all_dishes(self):
        return {dish._name: dish._price for dish in self._all_dishes} 

