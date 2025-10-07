from typing import List


def circular_shift(integer_x: int, integer_shift: int) -> str:
    list_chars: List[str] = list(str(integer_x))
    if integer_shift > len(list_chars):
        return "".join(reversed(list_chars))
    else:
        pivot_index: int = len(list_chars) - integer_shift
        return "".join(list_chars[pivot_index:] + list_chars[:pivot_index])