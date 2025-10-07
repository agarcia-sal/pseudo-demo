from typing import List


def hex_key(string_num: str) -> int:
    prime_digits_collection: List[str] = ['2', '3', '5', '7', 'B', 'D']
    count_prime_chars: int = 0
    loop_indices: int = 0
    while loop_indices < len(string_num):
        current_char: str = string_num[loop_indices]
        if current_char in prime_digits_collection:
            count_prime_chars += 1
        loop_indices += 1
    return count_prime_chars