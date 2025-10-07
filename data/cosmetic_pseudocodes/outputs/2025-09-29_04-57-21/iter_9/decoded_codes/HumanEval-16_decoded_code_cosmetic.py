from typing import List, Set


def count_distinct_characters(input_string: str) -> int:
    character_collection: List[str] = []
    processed_string: str = input_string.lower()

    for individual_char in processed_string:
        character_collection.append(individual_char)

    unique_characters: Set[str] = set()
    index: int = 0

    while index < len(character_collection):
        unique_characters.add(character_collection[index])
        index += 1

    return len(unique_characters)