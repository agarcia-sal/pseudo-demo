from typing import List


def hex_key(string_num: str) -> int:
    prime_chars: List[str] = ['2', '3', '5', '7', 'B', 'D']
    count_primes: int = 0
    position: int = 0

    while position < len(string_num):
        if string_num[position] in prime_chars:
            count_primes += 1
        position += 1

    return count_primes