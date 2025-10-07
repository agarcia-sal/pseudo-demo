from math import floor, sqrt

def factorize(n):
    fact = []
    i = 2
    while i <= floor(sqrt(n)) + 1:
        if n % i == 0:
            fact.append(i)
            n = n // i
        else:
            i += 1
    if n > 1:
        fact.append(n)
    return fact