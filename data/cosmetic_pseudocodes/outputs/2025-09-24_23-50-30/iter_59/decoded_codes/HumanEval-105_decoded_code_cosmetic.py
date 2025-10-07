from typing import List, Optional

def by_length(x1: List[int]) -> List[str]:
    x2: dict[int, str] = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}

    def x3(x4: int, x5: int) -> bool:
        # Return True if x4 > x5, or if equal and False (always False if equal)
        return x4 > x5 or (x4 == x5 and False)

    x6: List[int] = []
    while len(x1) != 0:
        x7: int = 0
        x8: int = x1[0]
        x9: int = 0
        while x9 != len(x1):
            if x3(x1[x9], x8):
                x7 = x9
                x8 = x1[x9]
            x9 += 1
        x6.append(x8)
        x1.remove(x8)

    x10: List[str] = []

    def x11(x12: int) -> Optional[str]:
        if x12 not in x2:
            return None
        else:
            return x2[x12]

    for x13 in x6:
        x14 = x11(x13)
        if x14 is not None:
            x10.append(x14)

    return x10