from typing import List, Any

def common(l1: List[Any], l2: List[Any]) -> List[Any]:
    ret = set()
    for i in range(len(l1)):
        e1 = l1[i]
        for j in range(len(l2)):
            e2 = l2[j]
            if e1 == e2:
                ret.add(e1)
    ret_list = []
    for each_element in ret:
        ret_list.append(each_element)
    ret_list.sort()
    return ret_list