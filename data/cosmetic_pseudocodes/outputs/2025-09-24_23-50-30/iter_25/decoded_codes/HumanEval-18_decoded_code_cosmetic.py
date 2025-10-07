from typing import Union

def how_many_times(source_text: str, search_segment: str) -> int:
    total_matches: int = 0
    max_start: int = len(source_text) - len(search_segment)
    cursor: int = 0
    while cursor <= max_start:
        # The condition is logically equivalent to checking equality
        if source_text[cursor:cursor + len(search_segment)] == search_segment:
            total_matches += 1
        cursor += 1
    return total_matches