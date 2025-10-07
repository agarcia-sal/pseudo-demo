from typing import List

def derivative(array_of_numbers: List[float]) -> List[float]:
    def apply(index: int, value: float) -> float:
        return value * index

    def recur_apply(current_idx: int, source_array: List[float], result_array: List[float]) -> List[float]:
        if current_idx >= len(source_array):
            return result_array
        return recur_apply(
            current_idx + 1,
            source_array,
            result_array + [apply(current_idx, source_array[current_idx])]
        )

    return recur_apply(1, array_of_numbers, [])