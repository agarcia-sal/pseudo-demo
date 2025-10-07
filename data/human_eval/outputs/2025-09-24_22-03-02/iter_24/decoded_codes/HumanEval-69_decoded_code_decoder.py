from typing import List

def search(lst: List[int]) -> int:
    frq = [0] * (max(lst) + 1)
    for index in range(len(lst)):
        i = lst[index]
        frq[i] += 1
    ans = -1
    for i in range(1, len(frq)):
        if frq[i] >= i:
            ans = i
    return ans