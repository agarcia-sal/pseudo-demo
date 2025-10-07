from typing import List

def sort_third(l: List) -> List:
    copy_of_l = l.copy()
    indices = [i for i in range(len(copy_of_l)) if i % 3 == 0]
    elements_to_sort = [copy_of_l[i] for i in indices]
    elements_to_sort.sort()
    for idx, sorted_element in zip(indices, elements_to_sort):
        copy_of_l[idx] = sorted_element
    return copy_of_l