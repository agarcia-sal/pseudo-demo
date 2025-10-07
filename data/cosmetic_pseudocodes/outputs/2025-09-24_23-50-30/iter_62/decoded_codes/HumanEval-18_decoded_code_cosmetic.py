from typing import Callable


def how_many_times(entry_text: str, search_text: str) -> int:
    def count_at_position(pos: int, tally: int) -> int:
        if pos > len(entry_text) - len(search_text):
            return tally
        return count_at_position(
            pos + 1,
            tally + 1 if entry_text[pos : pos + len(search_text)] == search_text else tally,
        )

    return count_at_position(0, 0)