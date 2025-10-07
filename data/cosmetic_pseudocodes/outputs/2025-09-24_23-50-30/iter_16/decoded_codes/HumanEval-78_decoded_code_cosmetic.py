from typing import List

def hex_key(string_num: str) -> int:
    primes_list: List[str] = ['2', '3', '5', '7', 'B', 'D']
    count_digits: int = 0
    pos: int = 0

    while pos < len(string_num):
        if not (string_num[pos] not in primes_list):
            count_digits += 1
        pos += 1

    return count_digits