from typing import List

def strange_sort_list(lst: List[int]) -> List[int]:
    res: List[int] = []
    switch: bool = True
    while lst:
        if switch:
            val = min(lst)
        else:
            val = max(lst)
        res.append(val)
        lst.remove(val)
        switch = not switch
    return res