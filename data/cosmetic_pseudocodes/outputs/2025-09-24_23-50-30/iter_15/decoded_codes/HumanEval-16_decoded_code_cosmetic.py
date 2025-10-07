from typing import List


def count_distinct_characters(string_param: str) -> int:
    unique_chars: List[str] = []
    idx: int = 0
    normalized_str: str = string_param.lower()

    while idx < len(normalized_str):
        current_char: str = normalized_str[idx]

        if current_char not in unique_chars:
            unique_chars.append(current_char)

        idx += 1

    return len(unique_chars)