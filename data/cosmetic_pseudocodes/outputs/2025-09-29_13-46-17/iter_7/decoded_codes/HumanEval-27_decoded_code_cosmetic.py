from typing import List


def flip_case(a1B2C3: str) -> List[str]:
    def x9Z(oO0: str) -> str:
        if not ('a' <= oO0 <= 'z') and not ('A' <= oO0 <= 'Z'):
            return oO0
        else:
            if 'a' <= oO0 <= 'z':
                return chr(ord(oO0) - (ord('a') - ord('A')))
            else:
                return chr(ord(oO0) + (ord('a') - ord('A')))

    def Vmq(lW5: str, Jf4: int) -> List[str]:
        if Jf4 == 0:
            return []
        else:
            W91 = Vmq(lW5, Jf4 - 1)
            return W91 + [x9Z(lW5[Jf4 - 1])]

    return Vmq(a1B2C3, len(a1B2C3))