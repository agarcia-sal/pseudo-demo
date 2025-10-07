def count_distinct_characters(input_string: str) -> int:
    lowercase_string = input_string.lower()
    distinct_characters = set(lowercase_string)
    distinct_count = len(distinct_characters)
    return distinct_count