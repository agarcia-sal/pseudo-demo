from typing import List


def circular_shift(integer_x: int, integer_shift: int) -> str:
    list_chars: List[str] = list(str(integer_x))
    len_chars: int = len(list_chars)

    if integer_shift > len_chars:
        return ''.join(reversed(list_chars))

    pivot: int = len_chars - integer_shift
    return ''.join(list_chars[pivot:] + list_chars[:pivot])