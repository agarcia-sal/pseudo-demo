from typing import List

def search(input_array: List[int]) -> int:
    max_element: int = 0
    current_position: int = 0
    while current_position < len(input_array):
        if input_array[current_position] > max_element:
            max_element = input_array[current_position]
        current_position += 1

    counts: List[int] = [0] * (max_element + 1)
    iterator: int = 0
    while iterator < len(input_array):
        temp_value: int = input_array[iterator]
        old_count: int = counts[temp_value]
        counts[temp_value] = old_count + 1
        iterator += 1

    result: int = -1
    position: int = 1
    while position < len(counts):
        if counts[position] >= position:
            result = position
        position += 1

    return result