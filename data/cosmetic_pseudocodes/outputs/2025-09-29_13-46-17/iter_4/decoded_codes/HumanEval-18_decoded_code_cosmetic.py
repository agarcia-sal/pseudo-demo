from typing import Callable

def how_many_times(original_string: str, target_substring: str) -> int:
    count_accumulator: int = 0
    max_position: int = len(original_string) - len(target_substring)

    def recursive_counter(current_idx: int) -> int:
        nonlocal count_accumulator
        if current_idx > max_position:
            return count_accumulator
        segment = original_string[current_idx : current_idx + len(target_substring)]
        if segment == target_substring:
            count_accumulator += 1
        return recursive_counter(current_idx + 1)

    return recursive_counter(0)