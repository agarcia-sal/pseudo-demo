from typing import List

def hex_key(string_num: str) -> int:
    prime_digits: List[str] = ['2', '3', '5', '7', 'B', 'D']
    count_primes: int = 0
    i: int = 0
    length: int = len(string_num)
    while i < length:
        current_char: str = string_num[i]
        if current_char not in prime_digits:
            i += 1
            continue
        else:
            count_primes += 1
        i += 1
    return count_primes