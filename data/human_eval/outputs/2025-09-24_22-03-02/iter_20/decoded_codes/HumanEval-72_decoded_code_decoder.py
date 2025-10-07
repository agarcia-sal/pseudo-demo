from typing import List

def will_it_fly(q: List[int], w: int) -> bool:
    total_sum = 0
    for index in range(len(q)):
        total_sum += q[index]
    if total_sum > w:
        return False
    i, j = 0, len(q) - 1
    while i < j:
        if q[i] != q[j]:
            return False
        i += 1
        j -= 1
    return True