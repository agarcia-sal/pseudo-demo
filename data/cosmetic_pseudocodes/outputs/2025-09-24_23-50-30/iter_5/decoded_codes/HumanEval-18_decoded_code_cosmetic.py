from typing import Callable

def how_many_times(source_str: str, check_str: str) -> int:
    max_start_index: int = len(source_str) - len(check_str)

    def count_occurrences(current_pos: int) -> int:
        if current_pos > max_start_index:
            return 0
        return (1 if source_str[current_pos:current_pos + len(check_str)] == check_str else 0) + count_occurrences(current_pos + 1)

    total_matches: int = count_occurrences(0)
    return total_matches