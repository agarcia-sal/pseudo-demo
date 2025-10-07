from typing import Set

def count_distinct_characters(str_input: str) -> int:
    seen_chars: Set[str] = set()
    idx: int = 0
    lowered_string: str = str_input.lower()
    while idx < len(lowered_string):
        if lowered_string[idx] not in seen_chars:
            seen_chars.add(lowered_string[idx])
        idx += 1
    return len(seen_chars)