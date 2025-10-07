def hex_key(num) -> int:
    primes = ['2', '3', '5', '7', 'B', 'D']
    total = 0
    for c in num:
        if c in primes:
            total += 1
    return total