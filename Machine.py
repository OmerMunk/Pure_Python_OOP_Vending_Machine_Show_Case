from CashInventory import CashInventory
import threading

from general.Exceptions.exceptions import MachineEmpty

MAX_ITEMS = 10
MAX_SLOTS = 10

class Machine():

    __singleton_lock = threading.Lock()
    __singleton_instance = None

    @classmethod
    def instance(cls, ID, location, slot=None, items=None, balance=None):
        if not cls.__singleton_instance:
            with cls.__singleton_lock:
                if not cls.__singleton_instance:
                    cls.__singleton_instance = cls(ID, location, slot, items, balance)
        return cls.__singleton_instance

    def __init__(self, ID, location, slots=None, items=None, balance=None):
        self.balance = balance
        self.items = items
        self.ID = ID
        self.location = location
        self.slots = slots
        self.balance = CashInventory.instance()
        self.transactions = None

    def show_inv(self):
        if self.slots:
            inventory ={}
            for slot in self.slots:
                name = slot.product.name
                inventory[name] = slot.get_amount
            print(inventory)
        else:
            raise MachineEmpty

    def define_slot(self, ID, product):
        self.slots[ID] = product




