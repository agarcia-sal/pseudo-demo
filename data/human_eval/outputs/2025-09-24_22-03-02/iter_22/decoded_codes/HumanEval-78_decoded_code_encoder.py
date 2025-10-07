def hex_key(num: str) -> int:
    primes = ('2', '3', '5', '7', 'B', 'D')
    total = 0
    length = len(num)
    index = 0
    while index < length:
        current_char = num[index]
        is_prime = False
        prime_index = 0
        primes_length = len(primes)
        while prime_index < primes_length:
            if current_char == primes[prime_index]:
                is_prime = True
                break
            prime_index += 1
        if is_prime:
            total += 1
        index += 1
    return total