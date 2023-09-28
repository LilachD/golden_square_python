class OrderSummary():

    def __init__(self, order):
        self._order = order

    def sum_up(self):
        return sum(self._order._basket.values())

    def view(self): 
        items = []
        for item in self._order._basket.keys():
            item_amount = self._order._basket[item] / self._order._menu[item]
            items += round(item_amount) * [(item, self._order._menu[item])]
        return (items, ("Total", self.sum_up()))