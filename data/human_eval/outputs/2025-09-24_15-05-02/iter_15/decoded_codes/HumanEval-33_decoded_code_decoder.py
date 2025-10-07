from typing import List, Any

def sort_third(list_l: List[Any]) -> List[Any]:
    list_l = list(list_l)
    indices = [i for i in range(len(list_l)) if i % 3 == 0]
    sorted_vals = sorted(list_l[i] for i in indices)
    for idx, val in zip(indices, sorted_vals):
        list_l[idx] = val
    return list_l