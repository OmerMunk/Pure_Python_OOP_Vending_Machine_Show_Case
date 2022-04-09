#todo: maybe i will make it an interface? and not a class? why do i need instances of it? same for bill.

from Money import Money

VALID_COINS = [1, 2, 5, 10]

# implement Factor design pattern
class Coin(Money):
    def __init__(self, value):
        if self.validate(value):
            super().__init__(value)
        else:
            raise Exception("Unacceptable coin")

    def acceptable(self):
        print(VALID_COINS)

    @staticmethod
    def validate(value):
        return value in VALID_COINS

