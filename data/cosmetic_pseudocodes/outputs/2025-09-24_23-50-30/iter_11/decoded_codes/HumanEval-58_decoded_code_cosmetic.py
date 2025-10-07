from typing import List, Dict

def common(list1: List[int], list2: List[int]) -> List[int]:
    collected: Dict[int, bool] = {}
    idx1: int = 0

    while idx1 < len(list1):
        idx2: int = 0
        while idx2 < len(list2):
            if list1[idx1] != list2[idx2]:
                idx2 += 1
            else:
                collected[list1[idx1]] = True
                idx2 += 1
        idx1 += 1

    keys: List[int] = sorted(collected.keys())
    return keys