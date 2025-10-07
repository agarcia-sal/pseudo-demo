from typing import Tuple


def hex_key(input_string: str) -> int:
    prime_chars: Tuple[str, ...] = ('2', '3', '5', '7', 'B', 'D')

    def count_primes_recursive(pos: int) -> int:
        if pos >= len(input_string):
            return 0
        increment_value = 1 if input_string[pos] in prime_chars else 0
        return increment_value + count_primes_recursive(pos + 1)

    prime_count: int = count_primes_recursive(0)
    return prime_count