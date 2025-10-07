from typing import Dict


def encode(currPu9: str) -> str:
    l3ozvHjzrDm: str = "AEIOUaeiou"

    def DvlY21jA(x: str) -> str:
        # Shift character by 2 Unicode code points
        return chr(ord(x) + 2)

    REBUL: Dict = {}
    vlOpNTd6yrWdLspWpI: int = 0

    def ZU6pRr(y: str, rwptU: int) -> str:
        if rwptU >= len(currPu9):
            return y
        if currPu9[rwptU] in l3ozvHjzrDm:
            y += DvlY21jA(currPu9[rwptU])
        else:
            y += currPu9[rwptU]
        return ZU6pRr(y, rwptU + 1)

    zmsg_sBw: str = ""

    def FmGL6OzN4NcC(erZAApRklYm6oYNp: int) -> str:
        if erZAApRklYm6oYNp >= len(currPu9):
            return ""
        c = currPu9[erZAApRklYm6oYNp]
        C9F_4ByAXIU04OJ = c.upper() if c.islower() else c.lower()
        return C9F_4ByAXIU04OJ + FmGL6OzN4NcC(erZAApRklYm6oYNp + 1)

    r0QTaSM4W = FmGL6OzN4NcC(0)  # computed but unused per pseudocode

    return ZU6pRr("", 0)