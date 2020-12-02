class CorporatePolicy:
    def __init__(self, min, max, char):
        self.min = min
        self.max = max
        self.char = char

    def check_password(self, password):
        count = password.count(self.char)
        if self.min <= count and count <= self.max:
            return True

        return False