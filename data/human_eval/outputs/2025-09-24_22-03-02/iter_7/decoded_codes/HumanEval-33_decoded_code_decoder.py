from typing import List

def sort_third(l: List) -> List:
    l = l.copy()
    indices = [i for i in range(len(l)) if i % 3 == 0]
    sorted_elements = sorted(l[i] for i in indices)
    for i, val in zip(indices, sorted_elements):
        l[i] = val
    return l