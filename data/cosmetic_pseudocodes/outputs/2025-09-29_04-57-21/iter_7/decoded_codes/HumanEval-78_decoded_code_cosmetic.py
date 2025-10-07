from collections.abc import Sequence


def hex_key(character_sequence: Sequence[str]) -> int:
    prime_chars_collection = {'2', '3', '5', '7', 'B', 'D'}
    count_of_primes = 0
    position = 0
    while position < len(character_sequence):
        if character_sequence[position] in prime_chars_collection:
            count_of_primes += 1
        position += 1
    return count_of_primes