from typing import Dict


def count_distinct_characters(text: str) -> int:
    unique_chars: Dict[str, bool] = {}
    pointer: int = 0
    total_chars: int = len(text)

    while pointer < total_chars:
        current_char: str = text[pointer].lower()
        unique_chars[current_char] = True
        pointer += 1

    return len(unique_chars)