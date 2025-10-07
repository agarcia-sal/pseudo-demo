from typing import Set

def count_distinct_characters(string: str) -> int:
    lowercase_string: str = string.lower()
    distinct_characters: Set[str] = set(lowercase_string)
    count: int = len(distinct_characters)
    return count