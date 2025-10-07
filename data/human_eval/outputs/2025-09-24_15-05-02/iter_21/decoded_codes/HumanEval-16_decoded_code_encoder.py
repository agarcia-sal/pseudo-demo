from typing import Set


def count_distinct_characters(string: str) -> int:
    lower_string: str = string.lower()
    distinct_characters: Set[str] = set(lower_string)
    count: int = len(distinct_characters)
    return count