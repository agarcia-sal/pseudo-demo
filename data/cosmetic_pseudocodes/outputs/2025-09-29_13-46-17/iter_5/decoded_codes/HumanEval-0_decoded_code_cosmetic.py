from typing import List

def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    def inner_loop(current_outer_index: int, current_inner_index: int) -> bool:
        if current_inner_index > len(list_of_numbers) - 1:
            return False
        if current_outer_index != current_inner_index:
            delta = list_of_numbers[current_outer_index] - list_of_numbers[current_inner_index]
            abs_delta = abs(delta)  # equivalent to (delta^2)^0.5
            if abs_delta < threshold_value:
                return True
        return inner_loop(current_outer_index, current_inner_index + 1)

    def outer_loop(outer_index: int) -> bool:
        if outer_index > len(list_of_numbers) - 1:
            return False
        if inner_loop(outer_index, 0):
            return True
        return outer_loop(outer_index + 1)

    return outer_loop(0)