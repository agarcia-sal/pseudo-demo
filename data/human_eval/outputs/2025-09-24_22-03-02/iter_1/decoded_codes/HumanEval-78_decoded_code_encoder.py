def hex_key(num):
    primes = {'2', '3', '5', '7', 'B', 'D'}
    return sum(1 for char in num if char in primes)