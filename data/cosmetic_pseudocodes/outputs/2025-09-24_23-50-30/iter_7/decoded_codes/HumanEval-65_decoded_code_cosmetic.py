from typing import List


def circular_shift(integer_x: int, integer_shift: int) -> str:
    list_chars: List[str] = list(str(integer_x))
    length_chars = 0

    for _ in list_chars:
        length_chars += 1

    if not (integer_shift <= length_chars):
        reversed_chars: List[str] = []
        for idx in range(length_chars - 1, -1, -1):
            reversed_chars.append(list_chars[idx])

        result_string = ""
        for ch in reversed_chars:
            result_string += ch

        return result_string

    pivot = length_chars - integer_shift
    rotated_list: List[str] = []

    for idx in range(pivot, length_chars):
        rotated_list.append(list_chars[idx])

    for idx in range(pivot):
        rotated_list.append(list_chars[idx])

    final_output = ""
    for element in rotated_list:
        final_output += element

    return final_output