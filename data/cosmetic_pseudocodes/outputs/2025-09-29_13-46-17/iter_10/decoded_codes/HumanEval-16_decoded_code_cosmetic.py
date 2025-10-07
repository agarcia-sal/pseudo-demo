from typing import List


def count_distinct_characters(input_string: str) -> int:
    lowercased: str = input_string.lower()  # convert to lowercase for case-insensitive distinct count
    distinct_chars: List[str] = list(set(lowercased))
    return len(distinct_chars)