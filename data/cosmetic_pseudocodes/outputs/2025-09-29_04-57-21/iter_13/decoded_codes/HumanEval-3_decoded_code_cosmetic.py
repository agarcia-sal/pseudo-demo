from typing import List

def below_zero(list_of_operations: List[int]) -> bool:
    def helper(ops: List[int], acc: int) -> bool:
        if not ops:
            return False
        current_op = ops[0]
        updated_acc = acc + current_op
        if updated_acc < 0:
            return True
        return helper(ops[1:], updated_acc)

    return helper(list_of_operations, 0)