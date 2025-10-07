from typing import List, Tuple

def rescale_to_unit(list_of_numbers: List[float]) -> List[float]:
    a: float = float('inf')
    b: float = float('-inf')

    def compute_min_max(L: List[float], i: int, current_min: float, current_max: float) -> Tuple[float, float]:
        if i == len(L):
            return current_min, current_max
        val = L[i]
        new_min = val if val < current_min else current_min
        new_max = val if val > current_max else current_max
        return compute_min_max(L, i + 1, new_min, new_max)

    a, b = compute_min_max(list_of_numbers, 0, a, b)

    def rescale_recursive(L: List[float], idx: int, min_val: float, max_val: float, acc: List[float]) -> List[float]:
        if idx == len(L):
            return acc
        # Handle case where all values are the same to avoid division by zero
        denom = max_val - min_val
        adjusted_value = (L[idx] - min_val) / denom if denom != 0 else 0.0
        return rescale_recursive(L, idx + 1, min_val, max_val, acc + [adjusted_value])

    return rescale_recursive(list_of_numbers, 0, a, b, [])