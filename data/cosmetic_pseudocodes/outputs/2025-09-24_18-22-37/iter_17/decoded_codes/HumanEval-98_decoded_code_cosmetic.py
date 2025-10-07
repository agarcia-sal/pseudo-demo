def count_upper(original_text: str) -> int:
    tally: int = 0
    pos: int = 0
    length: int = len(original_text)
    while pos < length:
        current_char: str = original_text[pos]
        if current_char in {'A', 'E', 'I', 'O', 'U'}:
            tally += 1
        pos += 2
    return tally