from typing import List

def strange_sort_list(lst: List[int]) -> List[int]:
    res: List[int] = []
    switch: bool = True
    while lst:
        if switch:
            value = min(lst)
        else:
            value = max(lst)
        res.append(value)
        lst.remove(value)
        switch = not switch
    return res