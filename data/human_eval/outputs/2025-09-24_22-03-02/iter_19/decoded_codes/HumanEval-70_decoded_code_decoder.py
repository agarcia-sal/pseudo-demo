from typing import List

def strange_sort_list(lst: List[int]) -> List[int]:
    res: List[int] = []
    switch: bool = True
    while len(lst) > 0:
        if switch:
            minimum_value = lst[0]
            i = 1
            while i < len(lst):
                if lst[i] < minimum_value:
                    minimum_value = lst[i]
                i += 1
            res.append(minimum_value)
            j = 0
            while j < len(lst):
                if lst[j] == minimum_value:
                    lst.pop(j)
                    break
                j += 1
        else:
            maximum_value = lst[0]
            i = 1
            while i < len(lst):
                if lst[i] > maximum_value:
                    maximum_value = lst[i]
                i += 1
            res.append(maximum_value)
            j = 0
            while j < len(lst):
                if lst[j] == maximum_value:
                    lst.pop(j)
                    break
                j += 1
        switch = not switch
    return res