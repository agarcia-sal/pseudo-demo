import math

def sum_digits(n):
    return sum(int(d) for d in str(n))

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def process(lst):
    maxPrime = max((x for x in lst if isPrime(x)), default=0)
    return sum_digits(maxPrime)