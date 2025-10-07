from typing import Set

def hex_key(alpha_str: str) -> int:
    prime_chars: Set[str] = {'2', '3', '5', '7', 'B', 'D'}

    def count_primes(pos: int, accum: int) -> int:
        if pos >= len(alpha_str):
            return accum
        return count_primes(pos + 1, accum + (1 if alpha_str[pos] in prime_chars else 0))

    return count_primes(0, 0)