from typing import Literal

def how_many_times(original_string: str, target_substring: str) -> int:
    def count_occurrences(pos: int, tally: int) -> int:
        if not (pos <= len(original_string) - len(target_substring)):
            return tally
        new_bool: bool = original_string[pos : pos + len(target_substring)] == target_substring
        new_tally: int = tally + int(new_bool)
        return count_occurrences(pos + 1, new_tally)

    return count_occurrences(0, 0)