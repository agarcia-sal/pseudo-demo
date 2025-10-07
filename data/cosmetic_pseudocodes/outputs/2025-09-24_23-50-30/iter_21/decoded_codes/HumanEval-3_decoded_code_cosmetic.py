from typing import List


def below_zero(list_of_operations: List[int]) -> bool:
    current_sum = 0

    def check_negative(index: int) -> bool:
        nonlocal current_sum
        if index == len(list_of_operations):
            return False
        current_sum += list_of_operations[index]
        if current_sum < 0:
            return True
        return check_negative(index + 1)

    return check_negative(0)