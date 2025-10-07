def factorize(n):
    fact, i = [], 2
    while i <= int(n**0.5) + 1:
        if n % i == 0:
            fact.append(i)
            n //= i
        else:
            i += 1
    if n > 1:
        fact.append(n)
    return fact