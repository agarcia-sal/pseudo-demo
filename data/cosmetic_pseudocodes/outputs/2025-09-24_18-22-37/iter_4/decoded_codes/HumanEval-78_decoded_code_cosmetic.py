from typing import List

def hex_key(input_str: str) -> int:
    primes_collection: List[str] = ['2', '3', '5', '7', 'B', 'D']
    prime_counter: int = 0
    position: int = 0
    length: int = len(input_str)
    while position < length:
        if input_str[position] in primes_collection:
            prime_counter += 1
        position += 1
    return prime_counter