from typing import Set

def count_distinct_characters(input_string: str) -> int:
    """
    Count the number of distinct characters in the input string, case-insensitive.

    Args:
        input_string: The string to count distinct characters from.

    Returns:
        The count of unique characters ignoring case.
    """
    lowercase_string: str = input_string.lower()
    unique_characters: Set[str] = set(lowercase_string)
    return len(unique_characters)