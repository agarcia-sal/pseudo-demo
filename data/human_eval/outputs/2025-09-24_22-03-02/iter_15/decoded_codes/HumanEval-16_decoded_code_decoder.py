def count_distinct_characters(string: str) -> int:
    lowercase_string = string.lower()
    characters_set = set(lowercase_string)
    result = len(characters_set)
    return result