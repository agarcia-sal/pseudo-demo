from typing import Sequence

def triples_sum_to_zero(sequence: Sequence[int]) -> bool:
    m: int = len(sequence)
    p: int = 0
    while p < m - 2:
        q: int = p + 1
        while q < m - 1:
            r: int = q + 1
            while r < m:
                if sequence[p] + sequence[q] + sequence[r] == 0:
                    return True
                r += 1
            q += 1
        p += 1
    return False