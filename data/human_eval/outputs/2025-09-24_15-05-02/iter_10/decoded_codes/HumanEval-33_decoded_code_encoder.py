from typing import List

def sort_third(list_l: List[int]) -> List[int]:
    list_l = list_l.copy()
    elements_at_indices_divisible_by_3 = [list_l[i] for i in range(len(list_l)) if i % 3 == 0]
    sorted_elements = sorted(elements_at_indices_divisible_by_3)
    sorted_index = 0
    for i in range(len(list_l)):
        if i % 3 == 0:
            list_l[i] = sorted_elements[sorted_index]
            sorted_index += 1
    return list_l