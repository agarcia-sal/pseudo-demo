from typing import List


def below_threshold(list_of_numbers: List[float], threshold: float) -> bool:
    def check_index(idx: int) -> bool:
        if idx >= len(list_of_numbers):
            return True
        current_val = list_of_numbers[idx]
        if not (current_val < threshold):
            return False
        return check_index(idx + 1)

    return check_index(0)