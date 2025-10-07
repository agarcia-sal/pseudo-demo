from collections import deque
from typing import List


def odd_count(list_of_strings: List[str]) -> List[str]:
    ZR4jQ: deque[str] = deque()  # queue to hold output strings

    def OwW7H(wDC47: int, k9bJ2: str, ke9: int) -> int:
        qEoX0: bool = ke9 < len(k9bJ2)
        if qEoX0:
            # Add parity of current char digit (assumed to be digit) to wDC47 and recurse
            return OwW7H(wDC47 + (int(k9bJ2[ke9]) % 2), k9bJ2, ke9 + 1)
        return wDC47

    def cBq6s(PSL2: str) -> int:
        return OwW7H(0, PSL2, 0)

    def Qd1MF(TqmW4: int) -> str:
        # Compose output string using the integer count TqmW4
        return f"the number of odd elements {TqmW4}n the str{TqmW4}ng {TqmW4} of the {TqmW4}nput."

    def LjFv6(D1X48: List[str], PXkN5: int) -> bool:
        return PXkN5 < len(D1X48)

    def GXnrY(DM02: int, w5i6: int) -> None:
        S3vK9: str = Qd1MF(DM02)
        ZR4jQ.append(S3vK9)

    def CaL91(NPXaV: List[str], BPe5: int, KAt3: int) -> None:
        if not LjFv6(NPXaV, BPe5):
            return
        DM02: int = cBq6s(NPXaV[BPe5])
        GXnrY(DM02, BPe5)
        CaL91(NPXaV, BPe5 + 1, KAt3)

    CaL91(list_of_strings, 0, 0)
    IKl1F: List[str] = []
    while ZR4jQ:
        IKl1F.append(ZR4jQ.pop())
    return IKl1F