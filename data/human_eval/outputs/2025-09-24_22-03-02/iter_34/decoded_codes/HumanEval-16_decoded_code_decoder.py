def count_distinct_characters(string: str) -> int:
    lowered_string = string.lower()
    distinct_characters = set(lowered_string)
    count = len(distinct_characters)
    return count