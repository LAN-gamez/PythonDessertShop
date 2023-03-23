

tax_rate = 0.07


class Candy:

    def __init__(self, weight):
        self.weight = weight
    PRICE_PER_POUND = 475

    def total_cost(self):
        return self.weight * self.PRICE_PER_POUND

    def calculate_tax(self):
        return self.total_cost() * tax_rate


class Sundae(MenuItem):
    class HotFudge:
        cost = 125

    class CarmelSyrup:
        cost = 75

    class Peanuts:
        cost = 35

    class Coconut:
        cost = 20

    def __init__(self):
        self.toppings = []

    def add_topping(self, topping):
        self.toppings.append(topping)

    def calculate_cost(self):
        total = 340
        for topping in self.toppings:
            total += topping

