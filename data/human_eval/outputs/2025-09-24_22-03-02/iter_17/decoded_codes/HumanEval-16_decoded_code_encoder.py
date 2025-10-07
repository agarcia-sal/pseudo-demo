def count_distinct_characters(string: str) -> int:
    lower_string = string.lower()
    distinct_characters = set(lower_string)
    distinct_count = len(distinct_characters)
    return distinct_count