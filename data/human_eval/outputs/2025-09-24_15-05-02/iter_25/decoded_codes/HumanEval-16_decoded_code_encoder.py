from typing import Set

def count_distinct_characters(string: str) -> int:
    lowercased_string: str = string.lower()
    distinct_characters: Set[str] = set(lowercased_string)
    distinct_count: int = len(distinct_characters)
    return distinct_count