def hex_key(num: str) -> int:
    primes = ['2', '3', '5', '7', 'B', 'D']
    total = 0
    length_of_num = len(num)
    i = 0
    while i < length_of_num:
        current_char = num[i]
        is_prime_found = False
        j = 0
        length_of_primes = len(primes)
        while j < length_of_primes:
            if current_char == primes[j]:
                is_prime_found = True
                break
            j += 1
        if is_prime_found:
            total += 1
        i += 1
    return total