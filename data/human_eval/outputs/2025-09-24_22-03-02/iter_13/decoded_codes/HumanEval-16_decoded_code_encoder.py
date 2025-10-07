def count_distinct_characters(string) -> int:
    lowercase_string = string.lower()
    distinct_characters = set(lowercase_string)
    count = len(distinct_characters)
    return count