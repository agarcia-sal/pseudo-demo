from typing import List, Any

def sort_third(list_input: List[Any]) -> List[Any]:
    list_copy = list(list_input)
    indices_to_sort = [i for i in range(len(list_copy)) if i % 3 == 0]
    elements_to_sort = sorted(list_copy[i] for i in indices_to_sort)
    for idx, sorted_element in zip(indices_to_sort, elements_to_sort):
        list_copy[idx] = sorted_element
    return list_copy