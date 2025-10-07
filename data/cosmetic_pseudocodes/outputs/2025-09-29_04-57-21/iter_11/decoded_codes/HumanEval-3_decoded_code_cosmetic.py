from typing import List


def below_zero(list_of_operations: List[int]) -> bool:
    net_sum: int = 0
    index: int = 0
    while index < len(list_of_operations):
        current_value: int = list_of_operations[index]
        net_sum += current_value
        if net_sum < 0:
            return True
        index += 1
    return False