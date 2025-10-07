def factorize(n: int) -> list[int]:
    import math
    fact = []
    i = 2
    limit = int(math.sqrt(n)) + 1
    while i <= limit:
        remainder = n % i
        if remainder == 0:
            fact.append(i)
            n //= i
            limit = int(math.sqrt(n)) + 1
        else:
            i += 1
    if n > 1:
        fact.append(n)
    return fact