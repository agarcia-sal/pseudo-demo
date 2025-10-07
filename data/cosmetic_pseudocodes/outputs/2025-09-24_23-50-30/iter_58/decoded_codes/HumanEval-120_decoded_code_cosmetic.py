from typing import List

def maximum(x1: List[int], y2: int) -> List[int]:
    if y2 == 0:
        return []
    # Bubble sort x1 in-place
    for i3 in range(len(x1) - 1):
        for j4 in range(len(x1) - i3 - 1):
            if x1[j4] > x1[j4 + 1]:
                x1[j4], x1[j4 + 1] = x1[j4 + 1], x1[j4]
    # Collect the largest y2 elements
    p6: List[int] = []
    for m7 in range(len(x1) - y2, len(x1)):
        p6.append(x1[m7])
    return p6