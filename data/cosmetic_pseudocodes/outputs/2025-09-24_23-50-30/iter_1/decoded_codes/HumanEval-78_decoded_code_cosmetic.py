from typing import List

def hex_key(string_num: str) -> int:
    list_of_primes: List[str] = ['2', '3', '5', '7', 'B', 'D']
    total_prime_digits: int = 0
    position: int = 0
    while position < len(string_num):
        if string_num[position] in list_of_primes:
            total_prime_digits += 1
        position += 1
    return total_prime_digits