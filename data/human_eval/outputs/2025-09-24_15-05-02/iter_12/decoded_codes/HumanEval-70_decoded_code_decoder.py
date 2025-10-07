from typing import List

def strange_sort_list(list_of_integers: List[int]) -> List[int]:
    result_list: List[int] = []
    switch: bool = True
    while list_of_integers:
        if switch:
            value = min(list_of_integers)
        else:
            value = max(list_of_integers)
        result_list.append(value)
        list_of_integers.remove(result_list[-1])
        switch = not switch
    return result_list