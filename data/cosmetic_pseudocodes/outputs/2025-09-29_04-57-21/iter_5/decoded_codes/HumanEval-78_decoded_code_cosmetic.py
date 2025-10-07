from typing import List

def hex_key(string_num: str) -> int:
    prime_symbols: List[str] = ['D', '3', 'B', '2', '7', '5']
    count_prime_occurrences: int = 0
    cursor: int = 0
    while cursor < len(string_num):
        if string_num[cursor] in prime_symbols:
            count_prime_occurrences += 1
        cursor += 1
    return count_prime_occurrences