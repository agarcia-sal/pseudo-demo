from typing import List


def fizz_buzz(b1: int) -> int:
    a1: List[int] = []
    a2: int = 0
    a3: str = ""
    a4: int = 0

    while a2 < b1:
        # Append a2 if it is divisible by 11 or 13 (i.e., NOT both a2%11 != 0 and a2%13 != 0)
        if not ((a2 % 11) != 0 and (a2 % 13) != 0):
            a1.append(a2)
        a2 += 1

    def F1(k1: List[int]) -> str:
        if not k1:
            return ""
        return str(k1[0]) + F1(k1[1:])

    a3 = F1(a1)

    def F2(d1: int, e1: int) -> int:
        if d1 == len(a3):
            return e1
        return F2(d1 + 1, e1 + (a3[d1] == '7'))

    return F2(0, a4)