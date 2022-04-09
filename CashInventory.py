import threading

MONEY_DICT={
            'bils':{
                'hundreds': 100,
                'fifty': 50,
                'twenty': 20,
            },
            'coins':{
                'ten': 10,
                'five': 5,
                'two': 2,
                'one': 1
            }
        }

class CashInventory():

    __singleton_lock = threading.Lock()
    __singleton_instance = None

    @classmethod
    def instance(cls):
        if not cls.__singleton_instance:
            with cls.__singleton_lock:
                if not cls.__singleton_instance:
                    cls.__singleton_instance = cls()
        return cls.__singleton_instance


    def __init__(self,one=0, two=0, five=0,ten=0, twenty=0, fifty=0, hundred=0, two_hundred=0):
        self.one = one
        self.two = two
        self.five = five
        self.ten = ten
        self.twenty = twenty
        self.fifty = fifty
        self.hundred = hundred
        self.two_hundred = two_hundred

    def current_balance_detailed(self):
        balance_dictionary = {
            'coins': {
                'one': self.one,
                'two': self.two,
                'five': self.five,
                'ten': self.ten,
            },
            'bills': {
                'twenty': self.twenty,
                'fifty': self.fifty,
                'hundred': self.hundred,
                'two_hundred': self.two_hundred,
            }
        }
        return balance_dictionary

    def insert(self, given_value):
        for type in MONEY_DICT.keys():
            for key, value in MONEY_DICT[type].items():
                if given_value == value:
                    self.__setattr__(f"{key}", self.__getattribute__(f"{key}")+1)
                    return

    def produce_change(self, value, price):
        change_needed = value - price
        change = {
            'coins': {
                'one': 0,
                'two': 0,
                'five': 0,
                'ten': 0,
            },
            'bills': {
                'twenty': 0,
                'fifty': 0,
                'hundred': 0,
                'two_hundred': 0,
            }
        }

        for type in MONEY_DICT.keys():
            for key, value in MONEY_DICT[type].items():
                if change_needed >= value:
                    while self.current_balance_detailed()[type][key] > 0 and change_needed >= value:
                        change_needed -= value
                        change[type][key] += 1
        if change_needed == 0:
            for type in change.keys():
                for value, amount in change[type].items():
                    for _value,_amount in vars(self).items():
                        if amount > 0:
                            self.__setattr__(_value, _amount-1)
            return change
        else:
            return None






