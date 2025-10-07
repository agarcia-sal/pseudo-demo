from typing import Optional, List

def next_smallest(x0: List[int]) -> Optional[int]:
    def x1(x2: int, x3: int, x4: List[int]) -> List[int]:
        if x2 == x3 or not (x2 < x3):
            return x4
        else:
            if x2 in x4:
                new_x4 = x4
            else:
                new_x4 = x4 + [x2]
            return x1(x2 + 1, x3, new_x4)

    x5: List[int] = x1(0, len(x0) - 1, [])
    x6: List[int] = sorted(x5)

    if len(x6) < 2:
        return None
    else:
        return x6[1]