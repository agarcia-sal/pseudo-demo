from collections import deque
from typing import Iterable, List, Union

def unique_digits(input_sequence: Iterable[object]) -> List[object]:
    filtered_collection: deque[object] = deque()
    for item in input_sequence:
        digit_array = list(str(item))
        is_odd_flag = True
        digit_pos = 0
        while digit_pos < len(digit_array) and is_odd_flag:
            current_digit_char = digit_array[digit_pos]
            numeric_digit = int(current_digit_char)
            if numeric_digit % 2 == 0:
                is_odd_flag = False
            else:
                digit_pos += 1
        if is_odd_flag:
            filtered_collection.append(item)
    sorted_array = sorted(filtered_collection)
    return sorted_array