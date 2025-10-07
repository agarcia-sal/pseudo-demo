from typing import Optional, List, Set

def next_smallest(param_1: List[int]) -> Optional[int]:
    def helper(index_1: int, acc_1: List[int]) -> Optional[int]:
        if index_1 == len(acc_1):
            return None
        if index_1 == 0:
            return helper(index_1 + 1, acc_1)
        if index_1 == 1:
            return acc_1[1]
        return None

    set_1: Set[int] = set()
    list_1: List[int] = []
    i_1 = 0
    while i_1 < len(param_1):
        if param_1[i_1] not in set_1:
            set_1.add(param_1[i_1])
            list_1.append(param_1[i_1])
        i_1 += 1

    array_1 = list_1
    j_1 = 0
    while j_1 < len(array_1) - 1:
        k_1 = j_1 + 1
        while k_1 < len(array_1):
            if array_1[j_1] > array_1[k_1]:
                array_1[j_1], array_1[k_1] = array_1[k_1], array_1[j_1]
            k_1 += 1
        j_1 += 1

    return helper(0, array_1)