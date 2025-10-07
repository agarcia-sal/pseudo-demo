def count_distinct_characters(string: str) -> int:
    lowercase_string = string.lower()
    set_of_characters = set(lowercase_string)
    length_of_set = len(set_of_characters)
    return length_of_set