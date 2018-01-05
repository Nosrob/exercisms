from re import fullmatch

class Luhn(object):
    def __init__(self, number):
        self.number = number

    def is_valid(self):
        if not fullmatch("[0-9 ]{2,}", self.number): return False
        digits = [i for i in filter(lambda x: x.isdigit(),self.number)]

        tot = 0
        for i,v in enumerate(digits[::-1]):
            if not i % 2: tot += int(v)
            else: tot += int(v) * 2 - 9 if int(v) * 2 > 9 else int(v) * 2

        return not tot % 10
