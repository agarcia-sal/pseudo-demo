from typing import List

def hex_key(string_num: str) -> int:
    prime_chars: List[str] = ['2', '3', '5', '7', 'B', 'D']

    def count_primes_recursive(current_index: int, accumulator: int) -> int:
        if current_index >= len(string_num):
            return accumulator
        if string_num[current_index] in prime_chars:
            return count_primes_recursive(current_index + 1, accumulator + 1)
        return count_primes_recursive(current_index + 1, accumulator)

    return count_primes_recursive(0, 0)