from typing import List

def incr_list(input_array: List[int]) -> List[int]:
    output_sequence: List[int] = []
    iterator_index: int = 0
    element_count: int = len(input_array)
    while iterator_index < element_count:
        current_item: int = input_array[iterator_index]
        incremented_value: int = current_item + 1
        output_sequence.append(incremented_value)
        iterator_index += 1
    return output_sequence