from typing import List


def hex_key(alphanumeric_str: str) -> int:
    prime_chars_collection: List[str] = ['2', '3', '5', '7', 'B', 'D']
    prime_count_accumulator: int = 0

    def count_primes_recursive(position: int, total: int) -> int:
        if position >= len(alphanumeric_str):
            return total
        current_char = alphanumeric_str[position]
        increment_value = 1 if current_char in prime_chars_collection else 0
        return count_primes_recursive(position + 1, total + increment_value)

    return count_primes_recursive(0, prime_count_accumulator)