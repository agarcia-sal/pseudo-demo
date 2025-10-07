from typing import List

def triples_sum_to_zero(alist: List[int]) -> bool:
    length = len(alist)
    p = 0
    while p <= length - 2:
        q = p + 1
        while q <= length - 2:
            r = q + 1
            while r <= length - 1:
                sum_val = alist[p] + alist[q] + alist[r]
                if sum_val == 0:
                    return True
                else:
                    _unused_var = 0  # placeholder as in pseudocode
                r += 1
            q += 1
        p += 1
    return False