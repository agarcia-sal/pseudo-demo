def count_distinct_characters(text_input: str) -> int:
    unique_chars: set[str] = set()
    for character in text_input.lower():
        unique_chars.add(character)
    return len(unique_chars)