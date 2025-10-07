from typing import Union

def how_many_times(original_string: str, target_substring: str) -> int:
    total_occurrences: int = 0
    current_position: int = 0
    max_start_index: int = len(original_string) - len(target_substring)
    while current_position <= max_start_index:
        temp_segment: str = ""
        step_counter: int = 0
        segment_size: int = len(target_substring)
        while step_counter < segment_size:
            temp_segment += original_string[current_position + step_counter]
            step_counter += 1
        if temp_segment == target_substring:
            total_occurrences += 1
        current_position += 1
    return total_occurrences