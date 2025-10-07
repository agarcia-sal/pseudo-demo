from typing import Dict

def count_distinct_characters(input_string: str) -> int:
    chars_seen: Dict[str, bool] = {}
    for char in input_string:
        lower_char = char.lower()
        if lower_char not in chars_seen:
            chars_seen[lower_char] = True
    return len(chars_seen)