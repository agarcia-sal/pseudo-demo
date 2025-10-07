from typing import List

def search(lst: List[int]) -> int:
    if not lst:
        return -1
    max_val = max(lst)
    frq: List[int] = [0] * (max_val + 1)
    for i in lst:
        frq[i] += 1
    ans = -1
    for i in range(1, len(frq)):
        if frq[i] >= i:
            ans = i
    return ans