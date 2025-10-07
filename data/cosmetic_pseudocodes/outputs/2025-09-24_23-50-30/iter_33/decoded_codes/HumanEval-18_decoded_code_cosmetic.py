from typing import Callable


def how_many_times(source_text: str, search_pattern: str) -> int:
    def count_matches(position: int, tally: int) -> int:
        if position > len(source_text) - len(search_pattern):
            return tally
        return count_matches(
            position + 1,
            tally + (1 if source_text[position : position + len(search_pattern)] == search_pattern else 0),
        )

    return count_matches(0, 0)