from typing import List


def circular_shift(integer_x: int, integer_shift: int) -> str:
    list_chars: List[str] = list(str(integer_x))
    integer_length: int = len(list_chars)
    if integer_shift > integer_length:
        return "".join(reversed(list_chars))
    else:
        integer_split_point: int = integer_length - integer_shift
        list_tail: List[str] = list_chars[integer_split_point:integer_length]
        list_head: List[str] = list_chars[0:integer_split_point]
        return "".join(list_tail + list_head)