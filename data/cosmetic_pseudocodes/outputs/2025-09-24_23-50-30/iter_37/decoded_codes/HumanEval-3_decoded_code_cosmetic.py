from typing import List


def below_zero(list_of_operations: List[int]) -> bool:
    def check_ops(collection: List[int], index: int, current_sum: int) -> bool:
        if index >= len(collection):
            return False
        updated_sum = current_sum + collection[index]
        if updated_sum < 0:
            return True
        return check_ops(collection, index + 1, updated_sum)

    return check_ops(list_of_operations, 0, 0)