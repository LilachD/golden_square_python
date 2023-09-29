class OrderSummary():

    def __init__(self, order):
        self._order = order.show_basket()

    def sum_up(self):
        return sum([dish._price for dish in self._order])

    def view(self): 
        itemised_string = "\n".join([dish.format() for dish in self._order])
        return (f"{itemised_string}\n Total: £{self.sum_up()}")
    