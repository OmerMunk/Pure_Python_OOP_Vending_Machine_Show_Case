from Money import Money

class CreditCard(Money):
    def __init__(self, value, card_num, vaild_until, cvv, buyer_id, available):
        super().__init__(value)
        self.available = available
        self.buyer_id = buyer_id
        self.cvv = cvv
        self.card_num = card_num
        self.vaild_until = vaild_until
        
     