from typing import List

def circular_shift(integer_x: int, integer_shift: int) -> str:
    list_chars: List[str] = list(str(integer_x))
    length_val: int = len(list_chars)
    if integer_shift > length_val:
        reversed_list: List[str] = []
        index: int = length_val - 1
        while index >= 0:
            reversed_list.append(list_chars[index])
            index -= 1
        return ''.join(reversed_list)
    part_one: List[str] = list_chars[length_val - integer_shift : length_val]
    part_two: List[str] = list_chars[0 : length_val - integer_shift]
    combined_list: List[str] = []
    for element in part_one:
        combined_list.append(element)
    for element in part_two:
        combined_list.append(element)
    return ''.join(combined_list)