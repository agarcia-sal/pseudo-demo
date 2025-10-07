def count_distinct_characters(input_string: str) -> int:
    lowercase_string: str = input_string.lower()
    distinct_characters: set[str] = set(lowercase_string)
    distinct_count: int = len(distinct_characters)
    return distinct_count