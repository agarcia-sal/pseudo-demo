from typing import List

def hex_key(string_num: str) -> int:
    primes_collection: List[str] = ['2', '3', '5', '7', 'B', 'D']
    prime_count: int = 0
    current_pos: int = 0
    while current_pos < len(string_num):
        current_char: str = string_num[current_pos]
        if current_char in primes_collection:
            prime_count += 1
        current_pos += 1
    return prime_count