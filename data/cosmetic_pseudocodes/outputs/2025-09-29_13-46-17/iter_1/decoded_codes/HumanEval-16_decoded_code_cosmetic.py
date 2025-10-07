def count_distinct_characters(input_string: str) -> int:
    lowercase_string = input_string.lower()
    unique_chars: set[str] = set()
    for char in lowercase_string:
        unique_chars.add(char)
    return len(unique_chars)