def count_distinct_characters(source_text: str) -> int:
    unique_chars: set[str] = set()
    idx: int = 0
    length: int = len(source_text)
    while idx < length:
        current_char: str = source_text[idx].lower()
        if current_char not in unique_chars:
            unique_chars.add(current_char)
        idx += 1
    return len(unique_chars)