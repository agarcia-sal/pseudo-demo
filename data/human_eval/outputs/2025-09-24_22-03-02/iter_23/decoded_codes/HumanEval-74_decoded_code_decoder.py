from typing import List

def total_match(lst1: List[str], lst2: List[str]) -> List[str]:
    l1 = 0
    for index1 in range(len(lst1)):
        st = lst1[index1]
        l1 += len(st)

    l2 = 0
    for index2 in range(len(lst2)):
        st = lst2[index2]
        l2 += len(st)

    if l1 <= l2:
        return lst1
    else:
        return lst2