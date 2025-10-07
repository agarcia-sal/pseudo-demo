from typing import List

def incr_list(data: List[int]) -> List[int]:
    def helper(seq: List[int], idx: int, res: List[int]) -> List[int]:
        if idx == len(seq):
            return res
        else:
            return helper(seq, idx + 1, res + [seq[idx] + 1])
    return helper(data, 0, [])