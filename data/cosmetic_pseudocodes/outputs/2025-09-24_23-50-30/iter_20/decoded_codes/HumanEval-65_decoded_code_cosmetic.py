from typing import List


def circular_shift(integer_x: int, integer_shift: int) -> str:
    # Convert integer to list of characters
    list_chars: List[str] = list(str(integer_x))
    len_chars: int = len(list_chars)
    if not (integer_shift <= len_chars):
        # Return reversed string if shift is greater than length
        reversed_chars: List[str] = [list_chars[i] for i in range(len_chars - 1, -1, -1)]
        return ''.join(reversed_chars)
    split_point: int = len_chars - integer_shift
    part_one: List[str] = [list_chars[i] for i in range(split_point, len_chars)]
    part_two: List[str] = [list_chars[i] for i in range(split_point)]
    return ''.join(part_one + part_two)