from typing import List

def hex_key(string_num: str) -> int:
    prime_collection: List[str] = ['2', '3', '5', '7', 'B', 'D']
    count_prime_chars: int = 0
    position: int = 0
    while position < len(string_num):
        if string_num[position] in prime_collection:
            count_prime_chars += 1
        position += 1
    return count_prime_chars