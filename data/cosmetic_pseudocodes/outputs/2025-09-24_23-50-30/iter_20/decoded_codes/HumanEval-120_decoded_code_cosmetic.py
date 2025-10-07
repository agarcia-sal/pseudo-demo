from typing import List

def maximum(array_of_integers: List[int], positive_integer_k: int) -> List[int]:
    if positive_integer_k == 0:
        return []
    array_of_integers.sort()
    length_of_array = len(array_of_integers)
    start_index = length_of_array - positive_integer_k
    result_container: List[int] = []
    for index in range(start_index, length_of_array):
        result_container.append(array_of_integers[index])
    return result_container