from typing import List


def below_zero(list_of_operations: List[int]) -> bool:
    accumulator: int = 0

    def check_negative(index: int) -> bool:
        nonlocal accumulator
        if index == len(list_of_operations):
            return False
        if accumulator + list_of_operations[index] < 0:
            return True
        accumulator += list_of_operations[index]
        return check_negative(index + 1)

    return check_negative(0)