from typing import List


def below_zero(list_of_operations: List[int]) -> bool:
    def helper(idx: int, current_sum: int) -> bool:
        if idx >= len(list_of_operations):
            return False
        updated_accumulator = current_sum + list_of_operations[idx]
        if updated_accumulator < 0:
            return True
        return helper(idx + 1, updated_accumulator)

    return helper(0, 0)