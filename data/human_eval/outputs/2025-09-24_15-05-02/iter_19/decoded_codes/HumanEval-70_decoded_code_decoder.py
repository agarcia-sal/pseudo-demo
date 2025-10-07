from typing import List

def strange_sort_list(list_of_integers: List[int]) -> List[int]:
    result: List[int] = []
    switch: bool = True
    lst = list_of_integers[:]  # create a copy to avoid modifying the input
    while lst:
        if switch:
            val = min(lst)
        else:
            val = max(lst)
        result.append(val)
        lst.remove(val)
        switch = not switch
    return result