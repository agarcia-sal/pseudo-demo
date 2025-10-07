def count_distinct_characters(string: str) -> int:
    lower_string = string.lower()
    distinct_characters = set()
    for character in lower_string:
        distinct_characters.add(character)
    return len(distinct_characters)