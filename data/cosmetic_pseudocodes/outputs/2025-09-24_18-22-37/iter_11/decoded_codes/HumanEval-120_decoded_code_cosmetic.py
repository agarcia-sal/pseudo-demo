from typing import List

def maximum(array_of_integers: List[int], positive_integer_k: int) -> List[int]:
    if positive_integer_k == 0:
        return []
    sorted_array = sorted(array_of_integers)
    array_length = len(sorted_array)
    start_index = array_length - positive_integer_k
    result_list: List[int] = []
    iterator_index = start_index
    while iterator_index < array_length:
        result_list.append(sorted_array[iterator_index])
        iterator_index += 1
    return result_list