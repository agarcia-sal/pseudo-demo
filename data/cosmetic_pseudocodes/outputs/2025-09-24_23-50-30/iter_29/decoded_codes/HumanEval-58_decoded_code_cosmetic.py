from typing import List, Set

def common(alist: List[int], blist: List[int]) -> List[int]:
    intersect_set: Set[int] = set()
    index_a: int = 0
    while index_a < len(alist):
        index_b: int = 0
        while index_b < len(blist):
            if alist[index_a] == blist[index_b]:
                intersect_set.add(alist[index_a])
            index_b += 1
        index_a += 1
    sorted_result: List[int] = sorted(intersect_set)
    return sorted_result