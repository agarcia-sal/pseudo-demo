def hex_key(num: str) -> int:
    primes = ['2', '3', '5', '7', 'B', 'D']
    total = 0
    length = len(num)
    for i in range(length):
        current_char = num[i]
        is_prime_digit = False
        for j in range(len(primes)):
            if current_char == primes[j]:
                is_prime_digit = True
                break
        if is_prime_digit:
            total += 1
    return total