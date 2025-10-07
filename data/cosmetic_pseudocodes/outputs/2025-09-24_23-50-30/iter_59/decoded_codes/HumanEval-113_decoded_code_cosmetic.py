from typing import List

def odd_count(x1: List[str]) -> List[str]:
    x2: List[str] = []

    def x3(x4: str, x5: int) -> int:
        if x5 == len(x4):
            return 0
        x7: int = ord(x4[x5]) - ord('0')
        if (x7 - 2 * (x7 // 2)) != 1:
            return x3(x4, x5 + 1)
        return 1 + x3(x4, x5 + 1)

    for x9 in x1:
        x10: int = x3(x9, 0)
        x11: str = (
            "the number of odd elements "
            + str(x10)
            + "n the str"
            + str(x10)
            + "ng "
            + str(x10)
            + " of the "
            + str(x10)
            + "nput."
        )
        x2.append(x11)

    return x2