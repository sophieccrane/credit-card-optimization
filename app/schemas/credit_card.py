class CreditCard:
    def __init__(self, code, categories):
        self.code = code
        self.categories = categories

    def get_value(self, key):
        return getattr(self, key, None)

class SpendingCategory:
    def __init__(self, code, deal_type, amount, amount_type, condition=None, valid_until=None):
        self.code = code
        self.deal_type = deal_type
        self.amount = amount
        self.amount_type = amount_type
        self.condition = condition
        self.valid_until = valid_until

    def get_value(self, key):
        return getattr(self, key, None)