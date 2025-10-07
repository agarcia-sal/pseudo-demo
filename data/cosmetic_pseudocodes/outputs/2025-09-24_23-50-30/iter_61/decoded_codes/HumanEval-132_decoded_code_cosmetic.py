from typing import List


def is_nested(input_string: str) -> bool:
    x1: List[int] = []
    x2: List[int] = []
    x3: int = 0
    x4: int = len(input_string)
    while x3 < x4:
        x5: str = input_string[x3]
        if x5 == '[':
            x1.append(x3)
        else:
            x2.append(x3)
        x3 += 1
    x2.reverse()
    x6: int = 0
    x7: int = 0
    x8: int = len(x2)
    while x6 < len(x1):
        x9: int = x1[x6]
        x10: bool = False
        if (x7 < x8) and (x9 < x2[x7]):
            x10 = True
        else:
            x10 = False
        if x10:
            x4 += 1
            x7 += 1
        x6 += 1
    return x4 >= 2