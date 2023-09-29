class Menu():
    # User-facing: A list of dishes

    def __init__(self):
        self._all_dishes = []

    def add(self, dish):
        if dish in self._all_dishes:
            return f"{dish._name} has already been added to the menu"
        else:
            self._all_dishes.append(dish)

    def remove(self, dish):
        if dish in self._all_dishes:
            self._all_dishes.remove(dish)

    def show_all(self):
        return "\n".join([dish.format() for dish in self._all_dishes])

