from typing import Union

def circular_shift(integer_x: int, integer_shift: int) -> str:
    temp_str: str = str(integer_x)
    str_len: int = len(temp_str)

    if integer_shift > str_len:
        # Reverse the string by collecting characters in reverse order
        arr_chars: list[str] = []
        idx: int = str_len - 1
        while idx >= 0:
            arr_chars.append(temp_str[idx])
            idx -= 1

        reversed_str: str = ""
        idx = 0
        while idx < len(arr_chars):
            reversed_str += arr_chars[idx]
            idx += 1

        return reversed_str

    start_pos: int = str_len - integer_shift
    part_one: str = ""
    part_two: str = ""

    idx = start_pos
    while idx < str_len:
        part_one += temp_str[idx]
        idx += 1

    idx = 0
    while idx < start_pos:
        part_two += temp_str[idx]
        idx += 1

    return part_one + part_two