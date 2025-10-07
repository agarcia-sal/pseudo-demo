from typing import Set

def count_distinct_characters(input_string: str) -> int:
    character_collection: list[str] = []
    for symbol in input_string:
        character_collection.append(symbol.lower())

    unique_elements: Set[str] = set()
    index: int = 0
    while index < len(character_collection):
        unique_elements.add(character_collection[index])
        index += 1

    distinct_count: int = 0
    for element in unique_elements:
        distinct_count += 1

    return distinct_count