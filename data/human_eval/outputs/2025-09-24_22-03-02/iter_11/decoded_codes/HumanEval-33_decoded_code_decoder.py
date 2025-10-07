from typing import List, Any

def sort_third(l: List[Any]) -> List[Any]:
    l = list(l)
    third_elements = [l[i] for i in range(0, len(l), 3)]
    sorted_third_elements = sorted(third_elements)
    for idx, val in zip(range(0, len(l), 3), sorted_third_elements):
        l[idx] = val
    return l