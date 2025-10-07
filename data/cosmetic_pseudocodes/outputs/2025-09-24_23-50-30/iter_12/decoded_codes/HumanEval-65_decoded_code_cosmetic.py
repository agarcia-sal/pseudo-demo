from typing import List


def circular_shift(integer_x: int, integer_shift: int) -> str:
    digits_list: List[str] = list(str(integer_x))
    length_val: int = len(digits_list)

    if not (integer_shift <= length_val):
        return "".join(reversed(digits_list))

    split_index: int = length_val - integer_shift
    rotated_part: List[str] = digits_list[split_index:length_val]
    remaining_part: List[str] = digits_list[0:split_index]

    combined_list: List[str] = rotated_part + remaining_part
    return "".join(combined_list)