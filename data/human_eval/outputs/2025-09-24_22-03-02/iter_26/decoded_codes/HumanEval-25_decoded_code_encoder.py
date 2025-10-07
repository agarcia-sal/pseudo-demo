def factorize(n: int) -> list[int]:
    import math
    fact = []
    i = 2
    upper_limit = int(math.sqrt(n)) + 1
    while i <= upper_limit:
        if n % i == 0:
            fact.append(i)
            n //= i
            upper_limit = int(math.sqrt(n)) + 1
        else:
            i += 1
    if n > 1:
        fact.append(n)
    return fact