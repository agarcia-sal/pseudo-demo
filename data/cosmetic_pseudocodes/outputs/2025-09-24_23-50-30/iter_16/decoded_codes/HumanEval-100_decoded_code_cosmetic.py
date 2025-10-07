from typing import List

def make_a_pile(dim: int) -> List[int]:
    seq: List[int] = []
    cnt: int = 0
    while cnt < dim:
        seq.append(dim + cnt + cnt)
        cnt += 1
    return seq