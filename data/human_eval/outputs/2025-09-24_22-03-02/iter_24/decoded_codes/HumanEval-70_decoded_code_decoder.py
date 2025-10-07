from typing import List

def strange_sort_list(lst: List[int]) -> List[int]:
    res = []
    switch = True
    while lst != []:
        if switch == True:
            current_value = min(lst)
        else:
            current_value = max(lst)
        res.append(current_value)
        lst.remove(current_value)
        switch = not switch
    return res