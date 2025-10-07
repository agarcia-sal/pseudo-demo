from typing import Set

def count_distinct_characters(input_string: str) -> int:
    seen_chars: Set[str] = set()
    index_counter: int = 1
    length_input: int = len(input_string)

    while index_counter <= length_input:
        current_char: str = input_string[index_counter - 1].lower()
        if current_char not in seen_chars:
            seen_chars.add(current_char)
        index_counter += 1

    return len(seen_chars)