from typing import List, Optional

def rolling_max(seq_elements: List[int]) -> List[int]:
    def aux(idx: int, curr_max: Optional[int], acc: List[int]) -> List[int]:
        if idx == len(seq_elements):
            return acc
        new_max = seq_elements[idx] if curr_max is None or seq_elements[idx] > curr_max else curr_max
        return aux(idx + 1, new_max, acc + [new_max])
    return aux(0, None, [])