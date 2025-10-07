from typing import Sequence

def hex_key(string_num: str) -> int:
    list_of_primes: Sequence[str] = ('2', '3', '5', '7', 'B', 'D')
    total_prime_digits: int = 0
    for index in range(len(string_num)):
        if string_num[index] in list_of_primes:
            total_prime_digits += 1
    return total_prime_digits