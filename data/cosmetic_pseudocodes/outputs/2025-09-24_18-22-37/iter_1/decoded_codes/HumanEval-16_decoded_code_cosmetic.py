def count_distinct_characters(input_string: str) -> int:
    lowercase_string = input_string.lower()
    character_set = set(lowercase_string)
    return len(character_set)