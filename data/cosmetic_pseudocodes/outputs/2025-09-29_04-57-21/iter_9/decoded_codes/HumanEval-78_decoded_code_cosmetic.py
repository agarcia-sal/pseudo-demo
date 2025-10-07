from typing import List


def hex_key(string_num: str) -> int:
    primes_collection: List[str] = ['2', '3', '5', '7', 'B', 'D']
    prime_digit_count: int = 0
    pos: int = 0
    while pos < len(string_num):
        current_char: str = string_num[pos]
        if current_char in primes_collection:
            prime_digit_count += 1
        pos += 1
    return prime_digit_count