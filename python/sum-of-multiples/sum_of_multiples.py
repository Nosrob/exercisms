def sum_of_multiples(limit, multiples):
    return sum(set(x for multiple in multiples for x in range(0,limit,multiple)))
