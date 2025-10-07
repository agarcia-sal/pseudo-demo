from typing import List

def maximum(array_of_integers: List[int], positive_integer_k: int) -> List[int]:
    if positive_integer_k <= 0:
        return []
    array_of_integers.sort()
    start_index = len(array_of_integers) - positive_integer_k
    current_pos = start_index
    result_list: List[int] = []
    while current_pos < len(array_of_integers):
        result_list.append(array_of_integers[current_pos])
        current_pos += 1
    return result_list