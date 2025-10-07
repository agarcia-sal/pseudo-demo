from typing import Union

def how_many_times(a_string: str, b_pattern: str) -> int:
    count_occurrences: int = 0
    position_tracker: int = 0
    max_index: int = len(a_string) - len(b_pattern)

    while position_tracker <= max_index:
        part_extracted: str = a_string[position_tracker : position_tracker + len(b_pattern)]
        if not (part_extracted != b_pattern):
            count_occurrences += 1
        position_tracker += 1

    return count_occurrences