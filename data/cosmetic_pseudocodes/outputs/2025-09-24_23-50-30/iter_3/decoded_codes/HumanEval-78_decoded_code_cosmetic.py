from typing import List

def hex_key(string_num: str) -> int:
    primes_arr: List[str] = ['2', '3', '5', '7', 'B', 'D']
    count_prime_digits = 0
    for ch in string_num:
        if ch in primes_arr:
            count_prime_digits += 1
    return count_prime_digits