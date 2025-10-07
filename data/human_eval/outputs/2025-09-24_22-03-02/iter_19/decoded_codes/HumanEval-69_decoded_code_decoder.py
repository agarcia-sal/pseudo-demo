from typing import List

def search(lst: List[int]) -> int:
    frq: List[int] = []
    max_value: int = 0
    for index in range(len(lst)):
        if lst[index] > max_value:
            max_value = lst[index]
    for _ in range(max_value + 1):
        frq.append(0)
    for index_i in range(len(lst)):
        i = lst[index_i]
        frq[i] += 1
    ans = -1
    for i in range(1, len(frq)):
        if frq[i] >= i:
            ans = i
    return ans