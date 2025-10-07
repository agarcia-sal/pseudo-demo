from typing import List

def sort_array(seq: List[int]) -> List[int]:
    length = len(seq)
    if length == 0:
        return []
    total = seq[0] + seq[length - 1]
    desc_flag = (total % 2 == 0)
    return sorted(seq, reverse=desc_flag)