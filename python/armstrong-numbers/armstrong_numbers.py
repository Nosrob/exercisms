def is_armstrong(number):
    num = str(number)
    return sum([int(x) ** len(num) for x in num]) == number
