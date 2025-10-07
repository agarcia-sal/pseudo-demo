from typing import Set

def count_distinct_characters(input_string: str) -> int:
    if not isinstance(input_string, str):
        raise TypeError("input_string must be a string")
    lowercase_characters: str = input_string.lower()
    distinct_characters: Set[str] = set(lowercase_characters)
    count: int = len(distinct_characters)
    return count