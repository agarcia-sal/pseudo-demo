from typing import Callable

def how_many_times(original_string: str, target_substring: str) -> int:
    def count_accumulator(value: int, position: int) -> int:
        if position > len(original_string) - len(target_substring):
            return value
        segment = original_string[position : position + len(target_substring)]
        return count_accumulator(value + (1 if segment == target_substring else 0), position + 1)
    return count_accumulator(0, 0)