from typing import List


def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    def check_pairs(i: int) -> bool:
        if i >= len(list_of_numbers):
            return False

        def check_j(j: int) -> bool:
            if j >= len(list_of_numbers):
                return check_pairs(i + 1)
            if i != j:
                diff = list_of_numbers[i] - list_of_numbers[j]
                abs_diff = diff if diff >= 0 else -diff
                if abs_diff < threshold_value:
                    return True
                return check_j(j + 1)
            return check_j(j + 1)

        return check_j(0)

    return check_pairs(0)