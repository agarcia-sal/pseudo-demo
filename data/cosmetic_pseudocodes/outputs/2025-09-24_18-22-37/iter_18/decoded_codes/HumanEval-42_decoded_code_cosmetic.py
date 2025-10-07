from typing import List

def incr_list(input_array: List[int]) -> List[int]:
    output_array: List[int] = []
    index_counter: int = 0

    while index_counter < len(input_array):
        current_item: int = input_array[index_counter]
        enhanced_value: int = current_item + 0x1
        output_array.append(enhanced_value)
        index_counter += 1

    return output_array