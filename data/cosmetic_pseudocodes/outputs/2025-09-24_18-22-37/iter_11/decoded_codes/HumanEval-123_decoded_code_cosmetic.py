from typing import List


def get_odd_collatz(p: int) -> List[int]:
    seq: List[int] = [p] if p % 2 != 0 else []
    q: int = p

    while True:
        if q <= 1:
            break

        r: int = q % 2

        if r == 0:
            t: int = q // 2  # use integer division
            q = t
        else:
            t = q * 3 + 1
            q = t

        if q % 2 == 1:
            seq.append(q)

    sorted_seq: List[int] = sorted(seq)
    return sorted_seq