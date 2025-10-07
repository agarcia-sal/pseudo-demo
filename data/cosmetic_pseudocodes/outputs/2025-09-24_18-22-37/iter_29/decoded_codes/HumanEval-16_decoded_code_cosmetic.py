def count_distinct_characters(data_string: str) -> int:
    seen_chars: set[str] = set()
    position_index: int = 0
    while position_index < len(data_string):
        current_char = data_string[position_index].lower()
        if current_char not in seen_chars:
            seen_chars.add(current_char)
        position_index += 1
    return len(seen_chars)