import math

units= ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven",
    "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["zero", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def say(number):
    if number < 0 or number >= 1e12: raise ValueError("Incorrect input")
    if number == 0: return "zero"
    text = ""

    if math.floor(number / 1e9) > 0:
        text = ' '.join([text, say(math.floor(number / 1e9)), "billion"])
        number = number % 1e9
    if math.floor(number / 1e6) > 0:
        text = ' '.join([text, say(math.floor(number / 1e6)), "million"])
        number = number % 1e6
    if math.floor(number / 1e3) > 0:
        text = ' '.join([text, say(math.floor(number / 1e3)), "thousand"])
        number = number % 1e3
    if math.floor(number / 1e2) > 0:
        text = ' '.join([text, say(math.floor(number / 1e2)), "hundred"])
        number = number % 1e2
    number = int(number)
    if number > 0:
        if len(text) > 0: text = ' '.join([text, "and"])
        if number < 20: text = ' '.join([text, units[number]])
        else:
            text = ' '.join([text, tens[int(math.floor(number / 10))]])
            if number % 10 > 0: text = '-'.join([text, units[number % 10]])

    return text.strip()
