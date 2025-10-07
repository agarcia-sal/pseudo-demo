from typing import List

def common(list1: List[int], list2: List[int]) -> List[int]:
    set_result = set()
    index_i = 0
    while index_i < len(list1):
        index_j = 0
        while index_j < len(list2):
            if list1[index_i] == list2[index_j]:
                set_result.add(list1[index_i])
                break
            index_j += 1
        index_i += 1
    return sorted(list(set_result))