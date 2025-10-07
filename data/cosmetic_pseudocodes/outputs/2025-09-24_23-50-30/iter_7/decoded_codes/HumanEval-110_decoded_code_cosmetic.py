from typing import List

def exchange(a: List[int], b: List[int]) -> str:
    i: int = 0
    j: int = 0

    def count_odds(L: List[int], idx: int) -> int:
        if idx == len(L):
            return 0
        cur = L[idx]
        # (1 - ((cur % 2) + 1) / 2) evaluates to 1 if odd, 0 if even
        return int(1 - ((cur % 2) + 1) / 2) + count_odds(L, idx + 1)

    def count_evens(M: List[int], pos: int) -> int:
        if pos == len(M):
            return 0
        val = M[pos]
        increment = 1 - (val % 2)  # 1 if even, 0 if odd
        return increment + count_evens(M, pos + 1)

    i = count_odds(a, 0)
    j = count_evens(b, 0)

    result: str = "NO"
    if not (j < i):
        result = "YES"
    return result