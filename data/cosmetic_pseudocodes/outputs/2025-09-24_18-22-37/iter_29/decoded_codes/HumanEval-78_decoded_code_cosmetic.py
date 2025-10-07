from typing import Sequence

def hex_key(wrapped_input: Sequence[str]) -> int:
    primal_chars = {'2', '3', '5', '7', 'B', 'D'}
    count_prime_chars = 0
    pos = 0
    length = len(wrapped_input)
    while pos <= length - 1:
        current_char = wrapped_input[pos]
        if current_char in primal_chars:
            count_prime_chars += 1
        pos += 1
    return count_prime_chars