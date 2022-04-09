from Money import Money

VALID_BILLS = [20, 50, 100, 200]


class Bill(Money):


    def __init__(self, value):
        if self.validate(value):
            super().__init__(value)
        else:
            raise Exception("Unacceptable bill")

    def acceptable(self):
        print(VALID_BILLS)

    @staticmethod
    def validate(value):
        return value in VALID_BILLS

