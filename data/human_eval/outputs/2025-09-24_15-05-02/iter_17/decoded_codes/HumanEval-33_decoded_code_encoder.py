from typing import List, Any

def sort_third(list_l: List[Any]) -> List[Any]:
    list_l = list_l[:]
    elements_at_multiples_of_three = [list_l[i] for i in range(len(list_l)) if i % 3 == 0]
    sorted_elements = sorted(elements_at_multiples_of_three)
    for i in range(len(list_l)):
        if i % 3 == 0:
            list_l[i] = sorted_elements[i // 3]
    return list_l