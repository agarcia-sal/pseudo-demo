from typing import List

def strange_sort_list(lst: List[int]) -> List[int]:
    res: List[int] = []
    switch: bool = True
    while lst != []:
        if switch:
            m = min(lst)
            res.append(m)
            lst.remove(m)
        else:
            m = max(lst)
            res.append(m)
            lst.remove(m)
        switch = not switch
    return res