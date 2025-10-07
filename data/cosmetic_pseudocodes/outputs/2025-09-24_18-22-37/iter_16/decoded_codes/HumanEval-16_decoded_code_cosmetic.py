from typing import Set

def count_distinct_characters(alphanumeric_sequence: str) -> int:
    transformed_sequence: str = ""
    unique_character_set: Set[str] = set()

    for index in range(len(alphanumeric_sequence)):
        current_symbol = alphanumeric_sequence[index]
        transformed_sequence += current_symbol.lower()

    for position in range(len(transformed_sequence)):
        present_character = transformed_sequence[position]
        if present_character not in unique_character_set:
            unique_character_set.add(present_character)

    return len(unique_character_set)