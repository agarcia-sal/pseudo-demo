from typing import List


def count_distinct_characters(input_string: str) -> int:
    character_set: List[str] = []
    index_counter: int = 0
    input_length: int = len(input_string)
    while index_counter < input_length:
        current_char: str = input_string[index_counter].lower()
        if current_char not in character_set:
            character_set.append(current_char)
        index_counter += 1
    return len(character_set)