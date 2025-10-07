from typing import Union


def how_many_times(text_input: str, search_fragment: str) -> int:
    total_occurrences: int = 0
    upper_limit: int = len(text_input) - len(search_fragment)
    position: int = 0
    while position <= upper_limit:
        current_segment: str = text_input[position : position + len(search_fragment)]
        if current_segment == search_fragment:
            total_occurrences += 1
        position += 1
    return total_occurrences