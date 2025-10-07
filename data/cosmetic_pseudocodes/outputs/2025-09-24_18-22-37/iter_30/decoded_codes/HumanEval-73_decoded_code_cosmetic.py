from typing import Sequence

def smallest_change(numbers: Sequence[int]) -> int:
    result = 0
    length_value = len(numbers)
    midpoint = (length_value // 2) - 1
    counter = 0
    while counter <= midpoint:
        left_element = numbers[counter]
        right_index = length_value - counter - 1
        right_element = numbers[right_index]
        if left_element != right_element:
            result += 1
        counter += 1
    return result