from typing import List

def hex_key(string_num: str) -> int:
    primes_list: List[str] = ['2', '3', '5', '7', 'B', 'D']
    prime_count: int = 0
    for pos in range(len(string_num)):
        current_char: str = string_num[pos]
        if current_char in primes_list:
            prime_count += 1
    return prime_count