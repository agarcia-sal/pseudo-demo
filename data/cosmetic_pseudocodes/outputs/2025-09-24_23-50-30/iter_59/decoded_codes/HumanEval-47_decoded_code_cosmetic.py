from typing import List, Union

def median(x1: List[Union[int, float]]) -> Union[int, float]:
    def x2(x3: List[Union[int, float]], x4: int) -> List[Union[int, float]]:
        if x4 == 0:
            return []
        else:
            return [x3[0]] + x2(x3[1:], x4 - 1)

    x5: List[Union[int, float]] = x2(sorted(x1), len(x1))
    x6: int = len(x5)
    if x6 % 2 != 0:
        return x5[x6 // 2]
    else:
        x7 = x5[(x6 // 2) - 1] + x5[x6 // 2]
        return x7 / 2.0