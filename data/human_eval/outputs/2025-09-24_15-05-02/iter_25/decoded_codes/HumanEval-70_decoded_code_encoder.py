from typing import List

def strange_sort_list(list_of_integers: List[int]) -> List[int]:
    result: List[int] = []
    switch: bool = True
    ints = list_of_integers[:]  # create a copy to avoid mutating input
    while ints:
        if switch:
            value = min(ints)
        else:
            value = max(ints)
        result.append(value)
        ints.remove(value)  # remove first occurrence of value
        switch = not switch
    return result