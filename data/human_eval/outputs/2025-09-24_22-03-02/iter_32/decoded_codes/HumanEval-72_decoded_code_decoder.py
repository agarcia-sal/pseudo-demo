from typing import List

def will_it_fly(q: List[int], w: int) -> bool:
    total_sum = 0
    index = 0
    while index < len(q):
        element = q[index]
        total_sum += element
        index += 1
    if total_sum > w:
        return False
    i = 0
    j = len(q) - 1
    while i < j:
        if q[i] != q[j]:
            return False
        i += 1
        j -= 1
    return True