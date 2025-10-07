from typing import Callable

def how_many_times(original_string: str, target_substring: str) -> int:
    def count_occurrences(currentPosition: int, currentCount: int) -> int:
        if currentPosition > len(original_string) - len(target_substring):
            return currentCount
        if original_string[currentPosition : currentPosition + len(target_substring)] == target_substring:
            return count_occurrences(currentPosition + 1, currentCount + 1)
        return count_occurrences(currentPosition + 1, currentCount)
    return count_occurrences(0, 0)