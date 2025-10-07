from typing import List

def search(list_of_integers: List[int]) -> int:
    if not list_of_integers:
        return -1
    max_value = max(list_of_integers)
    frq: List[int] = [0] * (max_value + 1)
    for i in list_of_integers:
        frq[i] += 1
    ans: int = -1
    for i in range(1, len(frq)):
        if frq[i] >= i:
            ans = i
    return ans