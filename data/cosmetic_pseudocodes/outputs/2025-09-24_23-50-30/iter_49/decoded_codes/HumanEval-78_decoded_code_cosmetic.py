from typing import Set


def hex_key(string_num: str) -> int:
    def count_prime_chars(current_pos: int, accum_count: int) -> int:
        if current_pos >= len(string_num):
            return accum_count
        prime_candidates: Set[str] = {'2', '3', '5', '7', 'B', 'D'}
        is_prime_char = string_num[current_pos] in prime_candidates
        updated_count = accum_count + (1 if is_prime_char else 0)
        return count_prime_chars(current_pos + 1, updated_count)

    return count_prime_chars(0, 0)