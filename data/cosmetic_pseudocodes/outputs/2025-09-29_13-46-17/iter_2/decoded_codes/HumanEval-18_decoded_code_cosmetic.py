from typing import Callable


def how_many_times(original_string: str, target_substring: str) -> int:
    def count_occurrences(current_index: int, total_found: int) -> int:
        if current_index > len(original_string) - len(target_substring):
            return total_found
        match = original_string[current_index : current_index + len(target_substring)] == target_substring
        return count_occurrences(current_index + 1, total_found + (1 if match else 0))

    return count_occurrences(0, 0)