from typing import List

def search(lst: List[int]) -> int:
    if not lst:
        return -1
    max_value = lst[0]
    index = 0
    length = len(lst)
    while index < length:
        if lst[index] > max_value:
            max_value = lst[index]
        index += 1
    frq = [0] * (max_value + 1)
    index = 0
    while index < length:
        i = lst[index]
        frq[i] += 1
        index += 1
    ans = -1
    i = 1
    frq_length = len(frq)
    while i < frq_length:
        if frq[i] >= i:
            ans = i
        i += 1
    return ans