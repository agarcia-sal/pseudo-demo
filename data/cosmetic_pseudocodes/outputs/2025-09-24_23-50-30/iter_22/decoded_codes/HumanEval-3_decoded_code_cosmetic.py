from typing import List


def below_zero(operations_list: List[int]) -> bool:
    accumulator = 0
    index = 0

    while index < len(operations_list):
        current_value = operations_list[index]
        accumulator += current_value

        if accumulator < 0:
            return True

        index += 1

    return False