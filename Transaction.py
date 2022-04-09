from Coin import Coin, VALID_COINS
from Bill import Bill, VALID_BILLS
from general.Exceptions.exceptions import NoChange, ProductUnavailable, NotEnoughMoneyForProduct, MoneyError


class Transaction:
    def __init__(self, machine=None, chosen=None, is_credit=None ,balance=None):
        self.is_credit = is_credit
        self.machine = machine
        self.chosen = chosen
        self.balance = balance
        self.change = 0

    def set_chosen(self, chosen):
        self.chosen = chosen

    def set_balance(self, balance):
        self.balance = balance

    def get_chosen(self):
        return self.chosen

    def get_balance(self):
        return self.balance

    def commit(self):
        if self.machine.slots[self.chosen].amount > 0 and self.machine.slots[self.chosen].price <= self.balance:
            self.change = self.balance - self.machine.slots[self.chosen].price
            if self.change > 0:
                change = self.machine.balance.produce_change(self.chosen.price, self.balance)
                if change is not None:
                    self.change = 0
                    self.machine.slots[self.chosen].amount -= 1
                    return change
                else:
                    raise NoChange
        else:
            if self.machine.slots[self.chosen].amount == 0:
                raise ProductUnavailable(self.chosen.ID)
                # print('product is unavailable, choose another please')
            else:
                # print(f"Price is: {self.machine.slots[self.chosen].price}\nYou have:{self.balance}")
                raise NotEnoughMoneyForProduct(self.chosen.product.price)

    def insert(self, article):
        if Coin.validate(article):
            self.balance += article
            self.machine.balance.insert(article)
        elif Bill.validate(article):
            self.balance += article
            self.machine.balance.insert(article)
        else:
            raise MoneyError

    def cancel(self):
        for attribute in vars(self):
            self.__delattr__(attribute)
