MAX_NUMBERS_ORDERED = 20


class Cart:
    def __init__(self):
        self.items = []

    def add_dvd(self, dvd):
        if len(self.items) >= MAX_NUMBERS_ORDERED:
            return False
        self.items.append(dvd)
        return True

    def remove_dvd(self, dvd):
        if dvd not in self.items:
            return False
        self.items.remove(dvd)
        return True

    def total_cost(self):
        return sum(dvd.cost for dvd in self.items)

    def total_cost_with_discount(self, percent):
        if not 0 <= percent <= 100:
            raise ValueError("Discount percent must be between 0 and 100")
        return self.total_cost() * (1 - percent / 100)

    def print_cart(self):
        if not self.items:
            print("The cart is empty")
            return

        print("***********************CART***********************")
        for index, dvd in enumerate(self.items, start=1):
            print(f"{index}. {dvd}")
        print(f"Total cost: {self.total_cost():.2f} $")
        print("**************************************************")
