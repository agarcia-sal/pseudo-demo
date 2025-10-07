from typing import Callable


def how_many_times(original_string: str, target_substring: str) -> int:
    def check_at(position: int) -> int:
        if position > len(original_string) - len(target_substring):
            return 0
        if original_string[position : position + len(target_substring)] != target_substring:
            return check_at(position + 1)
        return 1 + check_at(position + 1)

    tally: int = check_at(0)
    return tally