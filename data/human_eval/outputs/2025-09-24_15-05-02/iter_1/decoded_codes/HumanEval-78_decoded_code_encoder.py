def hex_key(num):
    primes = {'2', '3', '5', '7', 'B', 'D'}
    return sum(1 for d in num if d in primes)