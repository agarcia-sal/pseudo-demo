from typing import List

def common(l1: List, l2: List) -> List:
    ret = set()
    i = 0
    while i < len(l1):
        e1 = l1[i]
        j = 0
        while j < len(l2):
            e2 = l2[j]
            if e1 == e2:
                ret.add(e1)
            j += 1
        i += 1
    ret_list = []
    for item in ret:
        ret_list.append(item)
    ret_list.sort()
    return ret_list