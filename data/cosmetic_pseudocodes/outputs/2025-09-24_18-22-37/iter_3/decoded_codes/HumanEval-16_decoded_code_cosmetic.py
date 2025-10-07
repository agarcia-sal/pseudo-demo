from typing import Set


def count_distinct_characters(input_string: str) -> int:
    def helper(index: int, seen_chars: Set[str]) -> int:
        if index == len(input_string):
            return len(seen_chars)
        current_char = input_string[index].lower()
        if current_char not in seen_chars:
            return helper(index + 1, seen_chars | {current_char})
        return helper(index + 1, seen_chars)

    return helper(0, set())