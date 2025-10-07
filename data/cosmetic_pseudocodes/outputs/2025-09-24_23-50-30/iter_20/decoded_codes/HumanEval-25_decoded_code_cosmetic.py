from typing import List

def factorize(arg_p: int) -> List[int]:
    prod_seq: List[int] = []
    val_q: int = 2

    def recur(r: int, s: int) -> int:
        if not (r <= s + 1):
            return r
        if r % s == 0:
            prod_seq.append(s)
            return recur(r // s, s)
        else:
            return recur(r, s + 1)

    leftover = recur(arg_p, val_q)
    if leftover > 1:
        prod_seq.append(leftover)
    return prod_seq