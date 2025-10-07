from typing import List

def search(lst: List[int]) -> int:
    frq = [0] * (max(lst, default=0) + 1)
    for i in lst:
        frq[i] += 1
    ans = -1
    for i in range(1, len(frq)):
        if frq[i] >= i:
            ans = i
    return ans