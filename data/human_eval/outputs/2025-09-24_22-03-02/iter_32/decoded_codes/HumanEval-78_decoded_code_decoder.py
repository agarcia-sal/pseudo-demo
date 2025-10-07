def hex_key(num: str) -> int:
    primes = ['2', '3', '5', '7', 'B', 'D']
    total = 0
    index = 0
    length = len(num)
    while index < length:
        current_char = num[index]
        found_prime = False
        prime_index = 0
        while prime_index < len(primes):
            if current_char == primes[prime_index]:
                found_prime = True
                break
            prime_index += 1
        if found_prime:
            total += 1
        index += 1
    return total