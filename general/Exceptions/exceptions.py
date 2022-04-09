class VendingMachineExceptions(Exception):
    """A base class for all vending machine exceptions"""

    def __init__(self, massage, element=None):
        self.element = element
        self.massage = massage

    def __str__(self):
        if self.element is not None:
            return self.massage + ": " + str(self.element)
        else:
            return self.massage


class CustomerErrors(VendingMachineExceptions):
    """A base class for all customer errors"""

    def __init__(self, massage, customer_element=None):
        self.element = customer_element
        self.massage = massage


class PaymentErrors(VendingMachineExceptions):
    """A base class for all payment errors"""

    def __init__(self, massage, payment_element=None):
        self.element = payment_element
        self.massage = massage


class ProductErrors(VendingMachineExceptions):
    """A base class for all product errors"""

    def __init__(self, massage, product_element=None):
        self.element = product_element
        self.massage = massage


class ProductUnavailable(ProductErrors):
    """This exception will raise if the user tries to purchase a product that is unavailable"""

    def __init__(self, product_id):
        massage = "This product is currently unavailable"
        super().__init__(product_id, massage)


class NoChange(PaymentErrors):
    """This exception will raise if there is not enough change in the vending machine balance."""

    def __init__(self):
        massage = "We're sorry, we currently dont have enough change, try another product with a different price"
        super().__init__(massage)


class NotEnoughMoneyForProduct(PaymentErrors):
    """This exception will raise if the customer doesn't have enough money inserted to purchase the current product."""

    def __init__(self, product_price):
        massage = "We're sorry, the item you are trying to purchase cost more then you've inserted"
        super().__init__(product_price, massage)


class MoneyError(PaymentErrors):
    """This exception will raise if the customer inserted an unacceptable type of money or corrupted money."""

    def __init__(self):
        massage = "We're sorry, the type of money that you've inserted is unacceptable or corrupted, try again or " \
                  "something else "
        super().__init__(massage)



class MachineErrors(VendingMachineExceptions):
    """A base class for all machine errors"""

    def __init__(self, massage, machine_element=None):
        self.element = machine_element
        self.massage = massage


class MachineEmpty(ProductErrors):
    """This exception will raise if the machine is empty."""

    def __init__(self):
        massage = "The machine is currently empty"
        super().__init__(massage)
