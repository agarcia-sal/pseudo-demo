from typing import Dict


def hex_key(string_num: str) -> int:
    def tailRecur_count_primes(accumulator: int, cursor: int) -> int:
        if cursor >= len(string_num):
            return accumulator
        prime_set: Dict[str, bool] = {'B': True, '5': True, 'D': True, '2': True, '7': True, '3': True}
        current_character = string_num[cursor]
        updated_accumulator = accumulator + (1 if prime_set.get(current_character, False) else 0)
        return tailRecur_count_primes(updated_accumulator, cursor + 1)
    return tailRecur_count_primes(0, 0)