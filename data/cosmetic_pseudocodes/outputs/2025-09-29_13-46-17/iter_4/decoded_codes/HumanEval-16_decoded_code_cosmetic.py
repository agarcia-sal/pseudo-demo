from typing import Set


def count_distinct_characters(parameter_one: str) -> int:
    def inner_count(sequence: str, index: int, unique_chars: Set[str]) -> int:
        if index >= len(sequence):
            return len(unique_chars)
        current_element = sequence[index].lower()
        if current_element not in unique_chars:
            unique_chars = unique_chars | {current_element}  # create new set with added char
        return inner_count(sequence, index + 1, unique_chars)

    return inner_count(parameter_one, 0, set())