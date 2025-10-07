from typing import List, Any

def sort_third(list_input: List[Any]) -> List[Any]:
    lst = list(list_input)
    indices = [i for i in range(len(lst)) if i % 3 == 0]
    elements = [lst[i] for i in indices]
    elements.sort()
    for idx, val in zip(indices, elements):
        lst[idx] = val
    return lst