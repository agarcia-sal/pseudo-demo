from typing import Sequence

def hex_key(input_sequence: Sequence[str]) -> int:
    prime_chars = {'2', '3', '5', '7', 'B', 'D'}

    def count_primes(position: int, tally: int) -> int:
        if position >= len(input_sequence):
            return tally
        else:
            return count_primes(
                position + 1,
                tally + (1 if input_sequence[position] in prime_chars else 0)
            )

    return count_primes(0, 0)