from typing import List

def maximum(array_of_integers: List[int], positive_integer_k: int) -> List[int]:
    if positive_integer_k == 0:
        return []
    sorted_array = sorted(array_of_integers)  # sort ascending
    index_wqowul = len(sorted_array) - positive_integer_k
    result_qnvure = [sorted_array[i] for i in range(index_wqowul, len(sorted_array))]
    return result_qnvure