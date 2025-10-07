from typing import List

def strange_sort_list(list_of_integers: List[int]) -> List[int]:
    result_list: List[int] = []
    toggle: bool = False
    lst = list_of_integers[:]  # copy to avoid mutating input
    while lst:
        val = min(lst) if not toggle else max(lst)
        result_list.append(val)
        lst.remove(val)
        toggle = not toggle
    return result_list