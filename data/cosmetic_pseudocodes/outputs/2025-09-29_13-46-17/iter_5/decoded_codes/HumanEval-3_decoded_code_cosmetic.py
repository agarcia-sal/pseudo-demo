from typing import List

def below_zero(list_of_operations: List[int]) -> bool:
    def traverse_ops(idx_snake_case: int, accBalanceCamel: int) -> bool:
        if idx_snake_case == len(list_of_operations):
            return False
        updatedBalance = accBalanceCamel + list_of_operations[idx_snake_case]
        if updatedBalance < 0:
            return True
        return traverse_ops(idx_snake_case + 1, updatedBalance)

    return traverse_ops(0, 0)