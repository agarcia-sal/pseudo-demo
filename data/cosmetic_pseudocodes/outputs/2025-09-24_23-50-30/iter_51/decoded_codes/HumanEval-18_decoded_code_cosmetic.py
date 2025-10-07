from typing import Callable


def how_many_times(input_text: str, search_term: str) -> int:
    def count_occurrences(accumulator: int, current_pos: int) -> int:
        if current_pos > len(input_text) - len(search_term):
            return accumulator
        increment = 1 if input_text[current_pos : current_pos + len(search_term)] == search_term else 0
        return count_occurrences(accumulator + increment, current_pos + 1)

    return count_occurrences(0, 0)