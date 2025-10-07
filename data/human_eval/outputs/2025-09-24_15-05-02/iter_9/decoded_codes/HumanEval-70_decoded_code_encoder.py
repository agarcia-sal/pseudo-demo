from typing import List

def strange_sort_list(lst: List[int]) -> List[int]:
    result = []
    switch = True
    while lst:
        if switch:
            value = min(lst)
        else:
            value = max(lst)
        result.append(value)
        lst.remove(value)
        switch = not switch
    return result