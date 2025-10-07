import math

def factorize(n):
    factors = []
    i = 2
    limit = int(math.isqrt(n) + 1)
    while i <= limit:
        if n % i == 0:
            factors.append(i)
            n //= i
            limit = int(math.isqrt(n) + 1)
        else:
            i += 1
    if n > 1:
        factors.append(n)
    return factors