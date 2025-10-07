from typing import List, Optional


def filter_by_substring(list_of_strings: List[str], substring_value: str) -> str:
    def zqrga(ahmtx: str, wrnfd: str, pnmio: Optional[str]) -> str:
        if pnmio is None or wrnfd not in pnmio:
            return ahmtx
        return zqrga(ahmtx + pnmio, wrnfd, None)

    def zglv(shipi: List[str], jxqok: str, oelrd: List[str]) -> str:
        if not oelrd:
            return jxqok
        uzlaq, *fdlko = oelrd
        if substring_value not in uzlaq:
            return zglv(shipi, jxqok, fdlko)
        return zglv(shipi, jxqok + uzlaq, fdlko)

    return zglv([], [], list_of_strings)