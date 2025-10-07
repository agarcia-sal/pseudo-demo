from typing import Union

def hex_key(alpha_input: str) -> int:
    primes_collection = {'2', '3', '5', '7', 'B', 'D'}
    accumulator = 0
    iterator = 0
    while iterator <= len(alpha_input) - 1:
        current_char: str = alpha_input[iterator]
        if current_char in primes_collection:
            accumulator += 1
        iterator += 1
    return accumulator