def hex_key(num):
    primes = {'2', '3', '5', '7', 'B', 'D'}
    return sum(ch in primes for ch in num)