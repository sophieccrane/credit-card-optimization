class Lookup:
    def __init__(self, code, description):
        self.code = code
        self.description = description

    def get_value(self, key):
        return getattr(self, key, None)