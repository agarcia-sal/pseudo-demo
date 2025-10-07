from typing import List

def hex_key(string_num: str) -> int:
    count_prime: int = 0
    prime_chars: List[str] = ['2', '3', '5', '7', 'B', 'D']
    pos: int = 0

    while pos < len(string_num):
        if string_num[pos] in prime_chars:
            count_prime += 1
        pos += 1

    return count_prime