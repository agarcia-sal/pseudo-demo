from typing import List

def common(l1: List, l2: List) -> List:
    ret = set()
    for index1 in range(len(l1)):
        e1 = l1[index1]
        for index2 in range(len(l2)):
            e2 = l2[index2]
            if e1 == e2:
                ret.add(e1)
    ret_list = []
    for element in ret:
        ret_list.append(element)
    ret_list.sort()
    return ret_list