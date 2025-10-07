from typing import List

def strange_sort_list(list_of_integers: List[int]) -> List[int]:
    result_list = []
    switch = True
    integers = list_of_integers[:]
    while integers:
        if switch:
            value = min(integers)
        else:
            value = max(integers)
        result_list.append(value)
        integers.remove(value)
        switch = not switch
    return result_list