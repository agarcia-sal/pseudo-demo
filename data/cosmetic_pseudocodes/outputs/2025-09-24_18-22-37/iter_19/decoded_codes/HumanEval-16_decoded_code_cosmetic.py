from typing import Set


def count_distinct_characters(text_param: str) -> int:
    char_collection: str = text_param.lower()
    unique_characters: Set[str] = set()
    for i in range(len(char_collection)):
        if char_collection[i] not in unique_characters:
            unique_characters.add(char_collection[i])
    count_result: int = len(unique_characters)
    return count_result