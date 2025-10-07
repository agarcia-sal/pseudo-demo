from typing import List

def maximum(array_of_integers: List[int], k: int) -> List[int]:
    if k == 0:
        return []
    sorted_array = sorted(array_of_integers)
    start_index = len(sorted_array) - k
    result_list = [sorted_array[i] for i in range(start_index, len(sorted_array))]
    return result_list