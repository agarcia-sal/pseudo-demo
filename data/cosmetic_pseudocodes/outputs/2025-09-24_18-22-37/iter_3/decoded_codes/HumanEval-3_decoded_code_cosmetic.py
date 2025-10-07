from typing import List


def below_zero(list_of_operations: List[int]) -> bool:
    def subfunc(index: int, tally: int) -> bool:
        if index == len(list_of_operations):
            return False
        next_tally = tally + list_of_operations[index]
        if next_tally < 0:
            return True
        return subfunc(index + 1, next_tally)

    return subfunc(0, 0)