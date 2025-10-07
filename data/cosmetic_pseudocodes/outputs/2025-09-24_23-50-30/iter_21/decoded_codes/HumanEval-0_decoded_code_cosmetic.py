from typing import List

def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    length_numbers: int = len(list_of_numbers)

    def check_pairs(current_outer: int) -> bool:
        if current_outer >= length_numbers:
            return False

        def inner_loop(current_inner: int) -> bool:
            if current_inner >= length_numbers:
                return check_pairs(current_outer + 1)

            if current_outer != current_inner:
                delta: float = list_of_numbers[current_outer] - list_of_numbers[current_inner]
                if abs(delta) < threshold_value:
                    return True

            return inner_loop(current_inner + 1)

        return inner_loop(0)

    return check_pairs(0)