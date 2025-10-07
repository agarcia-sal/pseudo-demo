from typing import List


def generate_integers(param_x: int, param_y: int) -> List[int]:
    start_val: int = min(max(2, min(param_x, param_y)), 8)
    end_val: int = max(min(8, max(param_x, param_y)), 2)

    result_collection: List[int] = []
    iterator_k: int = start_val

    while iterator_k <= end_val:
        if (iterator_k % 2) == 0:
            result_collection.append(iterator_k)
        iterator_k += 1

    return result_collection