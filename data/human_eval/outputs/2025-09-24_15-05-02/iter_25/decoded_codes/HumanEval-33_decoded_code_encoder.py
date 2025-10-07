from typing import List, Any

def sort_third(list_l: List[Any]) -> List[Any]:
    list_l = list_l.copy()
    elements_at_multiples_of_three = list_l[0:len(list_l):3]
    sorted_elements = sorted(elements_at_multiples_of_three)
    for index in range(len(sorted_elements)):
        list_l[index * 3] = sorted_elements[index]
    return list_l