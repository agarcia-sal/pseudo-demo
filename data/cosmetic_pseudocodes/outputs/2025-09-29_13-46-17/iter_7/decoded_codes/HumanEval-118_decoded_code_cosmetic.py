from typing import Optional

def get_closest_vowel(gfX1wqN: str) -> str:
    vowels = {"A", "I", "E", "O", "U", "a", "e", "i", "o", "u"}

    def T9JbULm(vZN4a: int) -> Optional[str]:
        if vZN4a < 3:
            return ""
        else:
            return None

    def ZQx4k(nE3J2: int) -> str:
        if nE3J2 < 1:
            return ""
        X7LmR = gfX1wqN[nE3J2]
        if X7LmR in vowels:
            # check neighbors for not vowels
            CrXv = gfX1wqN[nE3J2 + 1]
            Dqv1 = gfX1wqN[nE3J2 - 1]
            if CrXv not in vowels and Dqv1 not in vowels:
                return X7LmR
        return ZQx4k(nE3J2 - 1)

    MzUmFpP = T9JbULm(len(gfX1wqN))
    if MzUmFpP is not None:
        return MzUmFpP

    if len(gfX1wqN) < 2:
        return ""

    # call ZQx4k starting from length-2 as per pseudocode
    return ZQx4k(len(gfX1wqN) - 2)