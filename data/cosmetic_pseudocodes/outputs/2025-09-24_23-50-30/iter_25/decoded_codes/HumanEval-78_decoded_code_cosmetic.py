from typing import Set

def hex_key(string_num: str) -> int:
    prime_set: Set[str] = {'B', '7', 'D', '5', '3', '2'}
    count_primes: int = 0
    pos: int = 0
    while pos < len(string_num):
        if string_num[pos] in prime_set:
            count_primes += 1
        pos += 1
    return count_primes