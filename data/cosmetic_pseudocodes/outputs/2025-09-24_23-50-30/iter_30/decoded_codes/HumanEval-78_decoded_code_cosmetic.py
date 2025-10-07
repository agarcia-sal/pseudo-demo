from typing import Set

def hex_key(input_str: str) -> int:
    prime_chars: Set[str] = {'B', '2', 'D', '7', '3', '5'}

    def count_primes(pos: int, acc: int) -> int:
        if pos >= len(input_str):
            return acc
        if input_str[pos] in prime_chars:
            return count_primes(pos + 1, acc + 1)
        return count_primes(pos + 1, acc)

    return count_primes(0, 0)