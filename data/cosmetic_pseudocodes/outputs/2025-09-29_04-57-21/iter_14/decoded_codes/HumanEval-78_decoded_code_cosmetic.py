from typing import List

def hex_key(string_num: str) -> int:
    primes: List[str] = ['2', '3', '5', '7', 'B', 'D']
    prime_counter: int = 0
    position: int = 0
    while position < len(string_num):
        current_character = string_num[position]
        if current_character in primes:
            prime_counter += 1
        position += 1
    return prime_counter