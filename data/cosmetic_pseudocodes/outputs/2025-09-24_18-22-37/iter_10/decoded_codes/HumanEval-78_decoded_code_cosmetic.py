from typing import Sequence

def hex_key(input_alpha: Sequence[str]) -> int:
    prime_collection = ('7', '2', 'D', '3', '5', 'B')
    sum_prime_matches = 0
    iterator_zeta = 0
    while iterator_zeta < len(input_alpha):
        current_char = input_alpha[iterator_zeta]
        if current_char in prime_collection:
            sum_prime_matches += 1
        iterator_zeta += 1
    return sum_prime_matches