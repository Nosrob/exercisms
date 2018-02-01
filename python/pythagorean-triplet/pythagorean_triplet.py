from math import gcd
from itertools import combinations

def primitive_triplets(number_in_triplet):
    # All Pythagorean triplets can be expressed in the form (m**2 − n**2, 2mn, m**2 + n**2), with m>n for integers m,n
    if number_in_triplet % 4: raise ValueError('Incorrect input')
    nm = ((n, m) for n, m in combinations(range(1, number_in_triplet//2 + 1), 2)
          if gcd(m, n) == 1
          and (m - n) % 2 != 0
          and number_in_triplet == 2*m*n)
    return set(tuple(sorted((m**2 - n**2, 2*m*n, m**2 + n**2))) for n, m in nm)


def triplets_in_range(range_start, range_end):
    return set(t for t in combinations(range(range_start, range_end + 1), 3) if is_triplet(t))

def is_triplet(triplet):
    a, b, c = sorted(triplet)
    return a**2 + b**2 == c**2
