hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
units = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

def numeral(number):
    numerals = "M" * int(number / 1000)
    number %= 1000
    numerals += hundreds[int(number / 100)]
    number %= 100
    numerals += tens[int(number / 10)]
    number %= 10
    numerals += units[int(number)]
    return numerals
