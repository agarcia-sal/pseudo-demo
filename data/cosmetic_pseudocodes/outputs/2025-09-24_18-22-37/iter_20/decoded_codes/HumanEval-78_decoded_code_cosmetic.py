from typing import Tuple

def hex_key(string_num: str) -> int:
    prime_digits: Tuple[str, ...] = ('2', '3', '5', '7', 'B', 'D')
    acc_prime_count: int = 0
    pos: int = 0
    str_len: int = len(string_num)
    while pos < str_len:
        curr_char: str = string_num[pos]
        if curr_char in prime_digits:
            acc_prime_count += 1
        pos += 1
    return acc_prime_count