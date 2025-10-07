from typing import List


def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    length_count: int = len(list_of_numbers)

    for outer_idx in range(length_count):
        for inner_idx in range(length_count):
            if outer_idx == inner_idx:
                continue
            diff_calc: float = list_of_numbers[outer_idx] - list_of_numbers[inner_idx]
            diff_calc = diff_calc if diff_calc >= 0 else -diff_calc
            if diff_calc < threshold_value:
                return True

    return False