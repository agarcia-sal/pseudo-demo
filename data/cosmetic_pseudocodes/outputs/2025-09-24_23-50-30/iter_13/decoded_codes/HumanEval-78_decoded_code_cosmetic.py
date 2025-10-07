from typing import Set

def hex_key(string_num: str) -> int:
    prime_characters: Set[str] = {'B', 'D', '3', '7', '2', '5'}
    count_primes: int = 0
    position: int = 0
    while position < len(string_num):
        if string_num[position] in prime_characters:
            count_primes += 1
        position += 1
    return count_primes