from typing import Callable

def how_many_times(original_string: str, target_substring: str) -> int:
    def count_occurrences(pos: int, total: int) -> int:
        if pos > len(original_string) - len(target_substring):
            return total
        if original_string[pos: pos + len(target_substring)] == target_substring:
            return count_occurrences(pos + 1, total + 1)
        return count_occurrences(pos + 1, total)

    return count_occurrences(0, 0)