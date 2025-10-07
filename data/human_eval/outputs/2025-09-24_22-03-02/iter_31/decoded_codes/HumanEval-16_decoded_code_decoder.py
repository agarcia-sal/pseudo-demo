def count_distinct_characters(string: str) -> int:
    lower_string = string.lower()
    char_set = set(lower_string)
    distinct_count = len(char_set)
    return distinct_count