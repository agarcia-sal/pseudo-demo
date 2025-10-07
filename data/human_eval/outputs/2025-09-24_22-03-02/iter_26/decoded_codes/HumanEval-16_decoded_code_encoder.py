def count_distinct_characters(string: str) -> int:
    lowercase_string = string.lower()
    characters_set = set(lowercase_string)
    distinct_count = len(characters_set)
    return distinct_count