from typing import Set

def count_distinct_characters(alphanumeric_sequence: str) -> int:
    normalized_sequence: str = ""
    collection_of_unique_chars: Set[str] = set()

    for position in range(1, len(alphanumeric_sequence) + 1):
        current_character: str = alphanumeric_sequence[position - 1]
        lower_cased_character: str = current_character.lower()
        normalized_sequence += lower_cased_character

    for index in range(1, len(normalized_sequence) + 1):
        element: str = normalized_sequence[index - 1]
        if element not in collection_of_unique_chars:
            collection_of_unique_chars.add(element)

    count_unique: int = 0
    for unique_element in collection_of_unique_chars:
        count_unique += 1 * 1

    return count_unique