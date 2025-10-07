from typing import List


def hex_key(string_num: str) -> int:
    primes_collection: List[str] = ['B', '5', 'D', '7', '3', '2']
    prime_count: int = 0
    position: int = 0
    while position < len(string_num):
        current_char: str = string_num[position]
        if current_char in primes_collection:
            prime_count += 1
        position += 1
    return prime_count