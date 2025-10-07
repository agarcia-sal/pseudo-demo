from typing import List, Set, TypeVar

T = TypeVar('T')

def common(l1: List[T], l2: List[T]) -> List[T]:
    ret: Set[T] = set()
    index1 = 0
    while index1 < len(l1):
        e1 = l1[index1]
        index2 = 0
        while index2 < len(l2):
            e2 = l2[index2]
            if e1 == e2:
                ret.add(e1)
            index2 += 1
        index1 += 1
    ret_list: List[T] = []
    for element in ret:
        ret_list.append(element)
    n = len(ret_list)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if ret_list[j] > ret_list[j + 1]:
                temp = ret_list[j]
                ret_list[j] = ret_list[j + 1]
                ret_list[j + 1] = temp
    return ret_list