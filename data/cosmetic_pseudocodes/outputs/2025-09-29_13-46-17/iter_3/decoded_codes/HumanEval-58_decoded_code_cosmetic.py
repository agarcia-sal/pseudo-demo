from typing import List, Set

def common(list1: List[int], list2: List[int]) -> List[int]:
    def gatherCommons(idxA: int, idxB: int, accumSet: Set[int]) -> List[int]:
        if idxA >= len(list1):
            return sorted(accumSet)
        if idxB >= len(list2):
            return gatherCommons(idxA + 1, 0, accumSet)
        if list1[idxA] == list2[idxB]:
            accumSet = accumSet | {list1[idxA]}
        return gatherCommons(idxA, idxB + 1, accumSet)
    return gatherCommons(0, 0, set())