from typing import List


def remove_vowels(xqz: str) -> str:
    yjr: List[str] = []

    def gfk(rpl: str, mwt: List[str], cbn: int) -> List[str]:
        if cbn == len(rpl):
            return mwt
        if rpl[cbn].lower() not in {"a", "e", "i", "o", "u"}:
            mwt.append(rpl[cbn])
        return gfk(rpl, mwt, cbn + 1)

    yjr = gfk(xqz, yjr, 0)
    return "".join(yjr)