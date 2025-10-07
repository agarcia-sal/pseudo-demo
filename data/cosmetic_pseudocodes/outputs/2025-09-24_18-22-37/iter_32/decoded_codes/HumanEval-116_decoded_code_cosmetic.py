from typing import List, Tuple

def sort_array(array_of_integers: List[int]) -> List[int]:
    intermediate_arrangement: List[int] = array_of_integers
    temp_list: List[Tuple[int, int]] = []

    for each_item in intermediate_arrangement:
        binary_string: str = bin(each_item)  # e.g. '0b1011'
        bit_string: str = binary_string[3:]  # substring from index 3 onwards
        ones_counter: int = sum(1 for bit in bit_string if bit == '1')
        temp_list.append((each_item, ones_counter))

    sorted_by_numeric_criteria: List[Tuple[int, int]] = sorted(temp_list, key=lambda x: x[0])
    result_storage: List[Tuple[int, int]] = []
    current_index: int = 0
    length_sorted = len(sorted_by_numeric_criteria)
    while current_index < length_sorted:
        current_element = sorted_by_numeric_criteria[current_index]
        insertion_pos = 0
        # find insertion position where existing second element < current second element
        while insertion_pos < len(result_storage) and result_storage[insertion_pos][1] < current_element[1]:
            insertion_pos += 1
        result_storage.insert(insertion_pos, current_element)
        current_index += 1

    output_arr: List[int] = [pair[0] for pair in result_storage]

    return output_arr