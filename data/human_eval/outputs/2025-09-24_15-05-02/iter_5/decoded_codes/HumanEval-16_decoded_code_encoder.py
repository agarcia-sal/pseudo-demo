def count_distinct_characters(string: str) -> int:
    lowercase_string = string.lower()
    distinct_characters = set(lowercase_string)
    number_of_distinct_characters = len(distinct_characters)
    return number_of_distinct_characters