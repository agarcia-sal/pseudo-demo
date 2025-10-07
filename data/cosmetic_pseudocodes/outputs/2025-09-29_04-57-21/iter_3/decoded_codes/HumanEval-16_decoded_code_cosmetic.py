def count_distinct_characters(input_string: str) -> int:
    lowercase_string: str = input_string.lower()
    unique_chars: set[str] = set()
    for character in lowercase_string:
        unique_chars.add(character)
    total_unique: int = len(unique_chars)
    return total_unique