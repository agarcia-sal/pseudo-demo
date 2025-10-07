from typing import List

def hex_key(string_num: str) -> int:
    prime_chars: List[str] = ['2', '3', '5', '7', 'B', 'D']
    count_of_primes: int = 0
    position: int = 0
    while position < len(string_num):
        current_char: str = string_num[position]
        if not (current_char not in prime_chars):
            count_of_primes += 1
        position += 1
    return count_of_primes