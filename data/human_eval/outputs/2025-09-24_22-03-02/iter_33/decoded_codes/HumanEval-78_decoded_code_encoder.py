def hex_key(num) -> int:
    primes = ['2', '3', '5', '7', 'B', 'D']
    total = 0
    length = len(num)
    i = 0
    while i < length:
        current_char = num[i]
        found_prime = False
        j = 0
        primes_length = len(primes)
        while j < primes_length and not found_prime:
            prime_char = primes[j]
            if current_char == prime_char:
                found_prime = True
            j += 1
        if found_prime:
            total += 1
        i += 1
    return total