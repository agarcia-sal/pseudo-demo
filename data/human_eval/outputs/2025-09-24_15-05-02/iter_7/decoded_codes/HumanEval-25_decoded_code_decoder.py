import math

def factorize(n):
    fact = []
    i = 2
    limit = math.isqrt(n) + 1
    while i <= limit and n > 1:
        if n % i == 0:
            fact.append(i)
            n //= i
            limit = math.isqrt(n) + 1
        else:
            i += 1
    if n > 1:
        fact.append(n)
    return fact