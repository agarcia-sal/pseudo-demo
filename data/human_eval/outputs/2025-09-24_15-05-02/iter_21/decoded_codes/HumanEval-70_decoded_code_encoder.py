from typing import List

def strange_sort_list(list_of_integers: List[int]) -> List[int]:
    result: List[int] = []
    switch: bool = True
    input_list: List[int] = list_of_integers.copy()
    while input_list:
        if switch:
            value = min(input_list)
        else:
            value = max(input_list)
        result.append(value)
        input_list.remove(value)
        switch = not switch
    return result