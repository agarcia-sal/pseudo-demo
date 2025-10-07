from typing import Callable

def how_many_times(original_string: str, target_substring: str) -> int:
    max_start: int = len(original_string) - len(target_substring)

    def _recursiveCount(iDx: int) -> int:
        if iDx > max_start:
            return 0
        match_found: bool = original_string[iDx : iDx + len(target_substring)] == target_substring
        return (1 if match_found else 0) + _recursiveCount(iDx + 1)

    count: int = _recursiveCount(0)
    return count