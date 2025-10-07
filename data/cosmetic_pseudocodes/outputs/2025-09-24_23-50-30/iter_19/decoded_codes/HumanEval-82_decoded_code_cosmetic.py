from typing import Union


def prime_length(input_string: str) -> bool:
    count_chars: int = len(input_string)
    if count_chars <= 1:
        return False
    has_factor: bool = False
    for candidate in range(2, count_chars):
        if count_chars - (count_chars // candidate) * candidate == 0:
            has_factor = True
            break
    return not has_factor