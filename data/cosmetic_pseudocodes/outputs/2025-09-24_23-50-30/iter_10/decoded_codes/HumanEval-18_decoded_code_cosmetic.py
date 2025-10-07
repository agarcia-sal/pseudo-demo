from typing import Callable


def how_many_times(original_string: str, target_substring: str) -> int:
    def count_matches(position: int, tally: int) -> int:
        if position > len(original_string) - len(target_substring):
            return tally
        return count_matches(
            position + 1,
            tally + (1 if original_string[position : position + len(target_substring)] == target_substring else 0),
        )

    return count_matches(0, 0)