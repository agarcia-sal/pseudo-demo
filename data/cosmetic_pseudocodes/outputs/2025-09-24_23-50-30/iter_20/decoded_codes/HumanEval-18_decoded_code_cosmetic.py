from typing import Callable

def how_many_times(original_string: str, target_substring: str) -> int:
    total_matches: int = 0
    max_start: int = len(original_string) - len(target_substring)

    def INDEX_LOOP(current_position: int) -> int:
        nonlocal total_matches
        if current_position > max_start:
            return total_matches
        if original_string[current_position:current_position + len(target_substring)] == target_substring:
            total_matches += 1
        return INDEX_LOOP(current_position + 1)

    return INDEX_LOOP(0)