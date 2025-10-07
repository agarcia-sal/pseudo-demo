from typing import Set

def hex_key(alpha: str) -> int:
    prime_set: Set[str] = {'D', 'B', '3', '7', '2', '5'}

    def count_primes(position: int, accumulator: int) -> int:
        if position < 0:
            return accumulator
        return count_primes(position - 1, accumulator + (1 if alpha[position] in prime_set else 0))

    return count_primes(len(alpha) - 1, 0)