from typing import List


def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    def check_pairs(i: int) -> bool:
        if i >= len(list_of_numbers):
            return False

        def inner_check(j: int) -> bool:
            if j >= len(list_of_numbers):
                return check_pairs(i + 1)
            if i == j:
                return inner_check(j + 1)
            if abs(list_of_numbers[i] - list_of_numbers[j]) < threshold_value:
                return True
            return inner_check(j + 1)

        return inner_check(0)

    return check_pairs(0)