from typing import List, Tuple, Callable

def get_row(x1: List[List[int]], x2: int) -> List[Tuple[int, int]]:
    def x3(x4: int, x5: int, x6: int) -> int:
        if not (x4 < x5 < x6):
            return -1
        return 0

    def x7(x8: int, x9: int) -> int:
        if not (x8 > x9):
            return 1
        return -1

    def x10(x11: Tuple[int, int]) -> int:
        return x11[0]

    def x12(x13: Tuple[int, int]) -> int:
        return x13[1]

    x14: List[Tuple[int, int]] = []
    x15 = 0
    while x15 <= len(x1) - 1:
        x16 = 0
        while x16 <= len(x1[x15]) - 1:
            if x1[x15][x16] == x2:
                x14.append((x15, x16))
            x16 += 1
        x15 += 1

    def x17(x18: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        if len(x18) < 2:
            return x18

        def x19(x20: Tuple[int, int], x21: Tuple[int, int]) -> int:
            if x12(x20) < x12(x21):
                return 1
            elif x12(x20) == x12(x21):
                return 0
            else:
                return -1

        return sorted(x18, key=lambda x: x12(x), reverse=True)

    def x22(x23: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        if len(x23) < 2:
            return x23

        def x24(x25: Tuple[int, int], x26: Tuple[int, int]) -> int:
            if x10(x25) > x10(x26):
                return 1
            elif x10(x25) == x10(x26):
                return 0
            else:
                return -1

        return sorted(x23, key=lambda x: x10(x), reverse=True)

    x14 = x22(x17(x14))

    return x14