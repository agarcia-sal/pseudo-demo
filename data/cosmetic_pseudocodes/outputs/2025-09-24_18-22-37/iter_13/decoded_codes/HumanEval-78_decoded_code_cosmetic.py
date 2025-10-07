from typing import List

def hex_key(input_string: str) -> int:
    prime_chars: List[str] = ['2', '3', '5', '7', 'B', 'D']
    count_primes: int = 0
    current_position: int = 0
    while current_position < len(input_string):
        current_character: str = input_string[current_position]
        if current_character in prime_chars:
            count_primes += 1
        current_position += 1
    return count_primes