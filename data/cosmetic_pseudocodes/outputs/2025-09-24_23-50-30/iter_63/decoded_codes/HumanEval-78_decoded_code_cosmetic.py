from typing import List


def hex_key(string_num: str) -> int:
    prime_chars: List[str] = ['2', '3', '5', '7', 'D', 'B']
    count_primes: int = 0
    pos: int = 0
    while pos < len(string_num):
        if string_num[pos] in prime_chars:
            count_primes += 1
        pos += 1
    return count_primes