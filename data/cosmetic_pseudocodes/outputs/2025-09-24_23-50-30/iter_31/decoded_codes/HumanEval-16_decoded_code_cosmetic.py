def count_distinct_characters(original_input: str) -> int:
    unique_elements: set[str] = set()
    cursor: int = 0
    normalized_input: str = original_input.lower()
    while cursor < len(normalized_input):
        unique_elements.add(normalized_input[cursor])
        cursor += 1
    return len(unique_elements)