def count_distinct_characters(input_string: str) -> int:
    lowercase_string: str = input_string.lower()
    unique_characters: set[str] = set(lowercase_string)
    return len(unique_characters)