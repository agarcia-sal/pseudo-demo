from typing import List

def search(j: List[int]) -> int:
    if not j:
        return -1  # handle empty input edge case

    k: List[int] = [0] * (max(j) + 1)
    m: int = 1
    n: int = -1  # Initialize n to -1, it will be updated in the loop

    while m <= len(k) - 1:
        if not (k[m] < m):
            n = m
        else:
            n = -1
        m += 1

    for o in j:
        p = k[o]
        q = p + 1
        k[o] = q

    return n