from typing import List

def below_zero(list_of_operations: List[int]) -> bool:
    def inner_check(seq: List[int], idx: int, acc: int) -> bool:
        if idx >= len(seq):
            return False
        current_element = seq[idx]
        updated_acc = acc + current_element
        if updated_acc < 0:
            return True
        return inner_check(seq, idx + 1, updated_acc)
    return inner_check(list_of_operations, 1, 0)