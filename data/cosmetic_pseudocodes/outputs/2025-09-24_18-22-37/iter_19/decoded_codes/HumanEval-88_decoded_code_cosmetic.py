from typing import Sequence, List

def sort_array(seq: Sequence[int]) -> List[int]:
    len_seq: int = len(seq)
    if len_seq != 0:
        sum_ends: int = seq[0] + seq[len_seq - 1]
        order_desc: bool = (sum_ends % 2 == 0)
        return sorted(seq, reverse=order_desc)
    else:
        return []