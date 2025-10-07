from typing import List

def exchange(list_one: List[int], list_two: List[int]) -> str:
    nX3gfK: int = 0
    _vZr7BI: int = 0

    def accumulate_odds(L: List[int], idx: int) -> int:
        if idx >= len(L):
            return 0
        H71hkG = L[idx]
        fn15JB = (H71hkG % 2) == 1  # True if odd
        if fn15JB:
            ret3pr = 1 + accumulate_odds(L, idx + 1)
        else:
            ret3pr = accumulate_odds(L, idx + 1)
        return ret3pr

    def accumulate_evens(L: List[int], k: int) -> int:
        if k < 0:
            return 0
        cLJV57 = L[k]
        condition4 = (cLJV57 % 2) == 0  # True if even
        partialResult = accumulate_evens(L, k - 1)
        return partialResult + (1 if condition4 else 0)

    nX3gfK = accumulate_odds(list_one, 0)
    _vZr7BI = accumulate_evens(list_two, len(list_two) - 1)

    if _vZr7BI - nX3gfK >= 0:
        return "YES"
    return "NO"