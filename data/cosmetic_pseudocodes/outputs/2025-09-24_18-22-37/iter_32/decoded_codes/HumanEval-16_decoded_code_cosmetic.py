from typing import Sequence

def count_distinct_characters(alphanumeric_sequence: Sequence[str]) -> int:
    char_collection: list[str] = []
    unique_counter: int = 0

    for index in range(1, len(alphanumeric_sequence)):
        current_char: str = alphanumeric_sequence[index].lower()
        if current_char not in char_collection:
            char_collection.append(current_char)

    unique_counter = len(char_collection)
    return unique_counter