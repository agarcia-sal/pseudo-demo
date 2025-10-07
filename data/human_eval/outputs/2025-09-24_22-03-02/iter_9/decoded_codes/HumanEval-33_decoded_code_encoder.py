from typing import List

def sort_third(l: List) -> List:
    l = l[:]
    elements_at_multiples_of_three = [l[i] for i in range(0, len(l), 3)]
    sorted_elements = sorted(elements_at_multiples_of_three)
    for idx, val in zip(range(0, len(l), 3), sorted_elements):
        l[idx] = val
    return l