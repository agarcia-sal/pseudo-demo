from typing import List, Tuple

def rescale_to_unit(input_sequence: List[float]) -> List[float]:
    def find_bounds(idx: int, cur_min: float, cur_max: float) -> Tuple[float, float]:
        if idx == len(input_sequence):
            return cur_min, cur_max
        elem = input_sequence[idx]
        new_min = elem if elem < cur_min else cur_min
        new_max = elem if elem > cur_max else cur_max
        return find_bounds(idx + 1, new_min, new_max)

    def helper(index: int, min_val: float, max_val: float, accum: List[float]) -> List[float]:
        if index == len(input_sequence):
            return accum
        current_val = input_sequence[index]
        # Protect against division by zero if all elements equal
        normalized = (current_val - min_val) / (max_val - min_val) if max_val != min_val else 0.0
        return helper(index + 1, min_val, max_val, accum + [normalized])

    min_el, max_el = find_bounds(0, float('inf'), float('-inf'))
    return helper(0, min_el, max_el, [])