from typing import Set

def hex_key(input_alpha: str) -> int:
    prime_set: Set[str] = {'2', '3', '5', '7', 'B', 'D'}

    def count_primes_rec(pos: int, accum: int) -> int:
        if pos < len(input_alpha):
            return count_primes_rec(pos + 1, accum + (1 if input_alpha[pos] in prime_set else 0))
        else:
            return accum

    return count_primes_rec(0, 0)