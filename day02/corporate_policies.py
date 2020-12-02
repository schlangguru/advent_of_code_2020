class SledRentalCorporatePolicy:
    def __init__(self, min, max, char):
        self.min = min
        self.max = max
        self.char = char

    def check_password(self, password):
        count = password.count(self.char)
        if self.min <= count and count <= self.max:
            return True

        return False


class TobogganCorporatePolicy:
    def __init__(self, pos1, pos2, char):
        self.pos1 = pos1
        self.pos2 = pos2
        self.char = char

    def check_password(self, password):
        pos1_match = password[self.pos1 - 1] == self.char
        pos2_match = password[self.pos2 - 1] == self.char
        if  pos1_match != pos2_match:
            return True

        return False