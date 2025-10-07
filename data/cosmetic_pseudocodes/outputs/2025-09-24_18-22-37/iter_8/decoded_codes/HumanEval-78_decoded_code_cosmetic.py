from typing import Sequence

def hex_key(alpha_input: Sequence[str]) -> int:
    prime_collection = ('2', '3', '5', '7', 'B', 'D')
    count_primes_found: int = 0
    position_var: int = 0
    while position_var < len(alpha_input):
        current_char = alpha_input[position_var]
        if current_char in prime_collection:
            count_primes_found += 1
        position_var += 1
    return count_primes_found