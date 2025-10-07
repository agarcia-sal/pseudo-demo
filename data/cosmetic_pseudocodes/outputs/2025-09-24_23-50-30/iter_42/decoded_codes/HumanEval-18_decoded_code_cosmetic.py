from typing import Callable

def how_many_times(original_string: str, target_substring: str) -> int:
    def helper(curr_pos: int, tally: int) -> int:
        if curr_pos > len(original_string) - len(target_substring):
            return tally
        return helper(
            curr_pos + 1,
            tally + (1 if original_string[curr_pos:curr_pos + len(target_substring)] == target_substring else 0),
        )
    return helper(0, 0)