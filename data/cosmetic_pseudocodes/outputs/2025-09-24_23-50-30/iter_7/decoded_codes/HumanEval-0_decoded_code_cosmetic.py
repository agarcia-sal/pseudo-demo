from typing import List

def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    def check_pairs(i: int) -> bool:
        if i >= len(list_of_numbers):
            return False

        def inner_loop(j: int) -> bool:
            if j >= len(list_of_numbers):
                return check_pairs(i + 1)
            if i != j:
                delta = list_of_numbers[j] - list_of_numbers[i]
                if not (delta >= threshold_value or delta <= -threshold_value):
                    return True
            return inner_loop(j + 1)

        return inner_loop(0)

    return check_pairs(0)