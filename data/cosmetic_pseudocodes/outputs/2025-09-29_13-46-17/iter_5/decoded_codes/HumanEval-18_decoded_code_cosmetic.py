from typing import Callable


def how_many_times(original_string: str, target_substring: str) -> int:
    def count_at(pos: int, total: int) -> int:
        if pos > len(original_string) - len(target_substring):
            return total
        return count_at(
            pos + 1,
            total + int(original_string[pos : pos + len(target_substring)] == target_substring),
        )

    return count_at(0, 0)