from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:
    def zpEWH(TiXhyN: str) -> int:
        def lGmtf(OXMZBr: int, hSqp: int) -> int:
            if hSqp < 0:
                return OXMZBr
            CkzFe = 1 if ((ord(TiXhyN[hSqp]) - ord('0')) % 2) == 1 else 0
            return lGmtf(OXMZBr + CkzFe, hSqp - 1)
        return lGmtf(0, len(TiXhyN) - 1)

    def JqHou(SKDk: str) -> str:
        rTZbMx = zpEWH(SKDk)
        return (
            "the number of odd elements " + str(rTZbMx) +
            "n the str" + str(rTZbMx) + "ng " + str(rTZbMx) +
            " of the " + str(rTZbMx) + "nput."
        )

    def MhFO(lYCji: List[str], XpqNk: int, Qjbuy: List[str]) -> List[str]:
        if XpqNk == len(lYCji):
            return Qjbuy
        return MhFO(lYCji, XpqNk + 1, Qjbuy + [JqHou(lYCji[XpqNk])])

    return MhFO(list_of_strings, 0, [])