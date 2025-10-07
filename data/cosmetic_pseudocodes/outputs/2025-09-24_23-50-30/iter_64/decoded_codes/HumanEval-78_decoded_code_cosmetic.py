from typing import Set

def hex_key(str_input: str) -> int:
    prime_set: Set[str] = {'B', 'D', '5', '3', '2', '7'}

    def count_primes(idx: int, acc: int) -> int:
        if idx >= len(str_input):
            return acc
        if str_input[idx] in prime_set:
            return count_primes(idx + 1, acc + 1)
        return count_primes(idx + 1, acc)

    return count_primes(0, 0)