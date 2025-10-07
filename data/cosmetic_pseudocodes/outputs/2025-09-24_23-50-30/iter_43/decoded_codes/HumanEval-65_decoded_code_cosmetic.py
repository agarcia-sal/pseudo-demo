from typing import List


def circular_shift(integer_x: int, integer_shift: int) -> str:
    array_chars: List[str] = list(str(integer_x))
    integer_len: int = len(array_chars)
    if integer_shift > integer_len:
        # Reverse the entire list if shift is greater than length
        array_result: List[str] = [array_chars[i] for i in range(integer_len - 1, -1, -1)]
        return ''.join(array_result)
    else:
        integer_pos: int = integer_len - integer_shift
        array_head: List[str] = array_chars[integer_pos:integer_len]
        array_tail: List[str] = array_chars[0:integer_pos]
        return ''.join(array_head) + ''.join(array_tail)