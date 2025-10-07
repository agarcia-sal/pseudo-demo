from typing import List, Optional

def prod_signs(array_of_integers: List[int]) -> Optional[int]:
    def helper(index: int, neg_count: int) -> int:
        if index >= len(array_of_integers):
            return neg_count
        if array_of_integers[index] == 0:
            return -1
        updated_count = neg_count + (1 if array_of_integers[index] < 0 else 0)
        return helper(index + 1, updated_count)

    if not array_of_integers:
        return None

    negatives_count = helper(0, 0)
    if negatives_count == -1:
        result_sign = 0
    else:
        result_sign = -1 if negatives_count % 2 else 1

    total_magnitude = sum(abs(x) for x in array_of_integers)

    return result_sign * total_magnitude