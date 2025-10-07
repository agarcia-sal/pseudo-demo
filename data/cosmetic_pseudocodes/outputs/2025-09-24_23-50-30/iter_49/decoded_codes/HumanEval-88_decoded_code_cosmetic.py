from typing import Sequence, List

def sort_array(sequence: Sequence[int]) -> List[int]:
    def helper(sequence_inner: Sequence[int]) -> List[int]:
        length = len(sequence_inner)
        if length == 0:
            return []
        alpha = sequence_inner[0]
        beta = sequence_inner[-1]
        gamma = (alpha + beta) % 2
        order_flag = (gamma == 0)
        # ORDER_DESCENDING if order_flag else ORDER_ASCENDING
        # so reverse=True if order_flag else reverse=False
        return sorted(sequence_inner, reverse=order_flag)
    return helper(sequence)