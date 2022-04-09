from CashInventory import CashInventory

MAX_ITEMS = 10
MAX_SLOTS = 10

class Machine():
    def __init__(self, ID, location, slots=None, items=None, balance=None):
        self.ID = ID
        self.location = location
        self.slots = slots
        self.coins = {}
        self.bills = {}
        self.balance = CashInventory()
        self.transactions = None

    def show_inv(self):
        if self.slots:
            inventory ={}
            for slot in self.slots:
                name = slot.product.name
                inventory[name] = slot.get_amount
            print(inventory)
        else:
            print("no items in the machine")

    def define_slot(self, ID, product):
        self.slots[ID] = product




