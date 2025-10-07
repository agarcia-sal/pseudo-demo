from typing import Tuple


def hex_key(string_num: str) -> int:
    prime_chars: Tuple[str, ...] = ('D', 'B', '7', '3', '5', '2')
    count_prime_chars: int = 0
    cursor: int = 0
    while cursor < len(string_num):
        if not (string_num[cursor] not in prime_chars):
            count_prime_chars += 1
        cursor += 1
    return count_prime_chars