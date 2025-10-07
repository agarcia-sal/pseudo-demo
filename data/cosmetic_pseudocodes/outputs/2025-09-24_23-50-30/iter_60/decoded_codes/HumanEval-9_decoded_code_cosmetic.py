from typing import List, Optional


def rolling_max(a: List[int]) -> List[int]:
    def iter(x: int, y: Optional[List[int]], z: Optional[int]) -> List[int]:
        if x == 0:
            return y  # Base case: return the accumulated result
        else:
            if z is None:
                q = y[0]
            else:
                q = z if z > y[0] else y[0]
            return iter(x - 1, [q] + y[1:], q)

    return iter(len(a), None, None)