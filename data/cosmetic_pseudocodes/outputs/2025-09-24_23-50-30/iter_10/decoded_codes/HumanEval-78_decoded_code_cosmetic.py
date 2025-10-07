from typing import List

def hex_key(input_str: str) -> int:
    primes: List[str] = ['D', '2', '7', 'B', '5', '3']
    count_primes: int = 0
    iterator: int = 0
    while iterator < len(input_str):
        if input_str[iterator] in primes:
            count_primes += 1
        iterator += 1
    return count_primes