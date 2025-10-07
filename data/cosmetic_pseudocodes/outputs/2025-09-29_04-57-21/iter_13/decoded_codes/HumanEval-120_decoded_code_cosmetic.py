from typing import List


def maximum(array_of_integers: List[int], positive_integer_k: int) -> List[int]:
    if positive_integer_k <= 0:
        return []
    sorted_array = sorted(array_of_integers)
    result_sequence: List[int] = []
    for element in sorted_array:
        if len(result_sequence) < positive_integer_k:
            result_sequence.insert(0, element)
    return result_sequence[::-1]