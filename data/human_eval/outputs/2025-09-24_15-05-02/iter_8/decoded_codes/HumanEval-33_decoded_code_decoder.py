from typing import List, Any

def sort_third(list_l: List[Any]) -> List[Any]:
    mutable_list = list(list_l)
    indices = [i for i in range(len(mutable_list)) if i % 3 == 0]
    elements_to_sort = [mutable_list[i] for i in indices]
    elements_to_sort.sort()
    for idx, sorted_element in zip(indices, elements_to_sort):
        mutable_list[idx] = sorted_element
    return mutable_list