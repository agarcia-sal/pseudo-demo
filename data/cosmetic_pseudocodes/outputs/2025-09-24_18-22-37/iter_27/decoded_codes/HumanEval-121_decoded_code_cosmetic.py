from typing import List

def solution(array_of_numbers: List[int]) -> int:
    accumulated_sum: int = 0
    iterator_index: int = 0
    length: int = len(array_of_numbers)
    while iterator_index < length:
        current_value: int = array_of_numbers[iterator_index]
        is_index_even: bool = (iterator_index % 2) == 0
        is_value_odd: bool = (current_value % 2) != 0
        if is_index_even:
            if is_value_odd:
                accumulated_sum += current_value
        iterator_index += 1
    return accumulated_sum