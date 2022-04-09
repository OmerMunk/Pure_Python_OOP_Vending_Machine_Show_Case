from Machine import MAX_ITEMS

class Slot:
    def __init__(self, ID, product=None, amount=0):
        self.ID = ID
        self.product = product
        self.amount = amount

    def set_product(self, product):
        self.product = product

    def get_product(self):
        return self.product

    def set_amount(self, amount):
        if not (amount > MAX_ITEMS):
            self.amount = amount
            print(f"the new amount is {amount}")
        else:
            print(f"error, the maximum amount is {MAX_ITEMS}")

    def get_amount(self):
        return self.amount

    def add_item(self, amount=1):
        if not (self.amount+ amount > MAX_ITEMS):
            self.amount += amount
            print(f"the new amount is {amount}")
        else:
            print(f"error, the maximum amount is {MAX_ITEMS}")


