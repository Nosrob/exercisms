def sieve(limit):
    multiples, primes = set(), set()
    for i in range(2, limit+1):
        if i not in multiples:
            primes.add(i)
            multiples.update(range(i*i, limit+1, i))
    return sorted(primes)
