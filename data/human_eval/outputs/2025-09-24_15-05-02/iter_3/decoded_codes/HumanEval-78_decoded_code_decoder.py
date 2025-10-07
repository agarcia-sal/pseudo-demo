def hex_key(num: str) -> int:
    primes = {'2', '3', '5', '7', 'B', 'D'}  # Set of prime hex characters
    total = 0
    for char in num:
        if char.upper() in primes:
            total += 1
    return total