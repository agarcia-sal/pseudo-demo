from typing import Union

def how_many_times(original_string: str, search_substring: str) -> int:
    occurrence_count: int = 0
    max_start_index: int = len(original_string) - len(search_substring) + 1
    if max_start_index < 0:
        return 0
    for index in range(max_start_index):
        if original_string[index : index + len(search_substring)] == search_substring:
            occurrence_count += 1
    return occurrence_count