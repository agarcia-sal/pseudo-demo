from typing import List

def below_zero(list_of_operations: List[int]) -> bool:
    def recur_delta(seq: List[int], cursor: int, acc: int) -> bool:
        if cursor >= len(seq):
            return False
        updated_val = acc + seq[cursor]
        if updated_val < 0:
            return True
        return recur_delta(seq, cursor + 1, updated_val)
    return recur_delta(list_of_operations, 0, 0)