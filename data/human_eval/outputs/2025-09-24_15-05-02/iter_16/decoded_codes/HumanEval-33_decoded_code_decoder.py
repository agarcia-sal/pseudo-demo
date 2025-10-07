from typing import List, Any

def sort_third(list_l: List[Any]) -> List[Any]:
    list_copy = list_l[:]
    elements_at_multiples_of_three = [list_copy[i] for i in range(0, len(list_copy), 3)]
    elements_at_multiples_of_three.sort()
    for idx, value in zip(range(0, len(list_copy), 3), elements_at_multiples_of_three):
        list_copy[idx] = value
    return list_copy