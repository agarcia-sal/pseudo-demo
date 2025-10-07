from typing import Tuple


def hex_key(input_str: str) -> int:
    prime_chars: Tuple[str, ...] = ('B', 'D', '3', '7', '2', '5')

    def count_primes(current_idx: int, count_acc: int) -> int:
        if current_idx == len(input_str):
            return count_acc
        if input_str[current_idx] in prime_chars:
            return count_primes(current_idx + 1, count_acc + 1)
        return count_primes(current_idx + 1, count_acc)

    return count_primes(0, 0)