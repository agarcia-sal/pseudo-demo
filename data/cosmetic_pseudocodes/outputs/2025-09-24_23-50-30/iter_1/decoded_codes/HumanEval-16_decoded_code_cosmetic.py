from typing import List

def count_distinct_characters(input_string: str) -> int:
    seen_chars: List[str] = []
    for character in input_string:
        ch = character.lower()
        if ch not in seen_chars:
            seen_chars.append(ch)
    return len(seen_chars)