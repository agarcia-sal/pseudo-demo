def count_distinct_characters(string: str) -> int:
    lowercase_string = string.lower()
    distinct_characters = set(lowercase_string)
    return len(distinct_characters)