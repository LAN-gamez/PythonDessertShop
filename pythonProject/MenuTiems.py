
tax_rate = 0.07


class Candy:

    def __init__(self, weight):
        self.weight = weight
    PRICE_PER_POUND = 475

    def total_cost(self):
        return self.weight * self.PRICE_PER_POUND

    def calculate_tax(self):
        return self.total_cost() * tax_rate


class Cookies:

    def __init__(self, dozen):
        self.dozen = dozen
    PRICE_PER_DOZEN = 625

    def total_cost(self):
        return self.dozen * self.PRICE_PER_DOZEN

    def calculate_tax(self):
        return self.total_cost() * tax_rate


class IceCream:

    def __init__(self, scoop):
        self.scoop = scoop
    PRICE_PER_SCOOP = 170

    def total_cost(self):
        return self.scoop * self.PRICE_PER_SCOOP

    def calculate_tax(self):
        return self.total_cost() * tax_rate


class MenuItem:
    menu_item = []


class Sundae(MenuItem):
    PRICEFUDGE = 125
    PRICESTRAWBERRY = 75
    PRICECARAMEL = 50
    PRICEPEANUT = 35
    PRICECOCONUT = 20


    def __init__(self):
        self.toppings = []

    def add_topping(self, topping):
        self.toppings.append(topping)

    def calculate_cost(self):
        cost = IceCream.__init__(scoop=2)
        if hotFudge:

