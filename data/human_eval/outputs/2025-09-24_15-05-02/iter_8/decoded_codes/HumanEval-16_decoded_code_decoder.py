from typing import Set

def count_distinct_characters(input_string: str) -> int:
    lowercase_string: str = input_string.lower()
    set_of_characters: Set[str] = set(lowercase_string)
    return len(set_of_characters)