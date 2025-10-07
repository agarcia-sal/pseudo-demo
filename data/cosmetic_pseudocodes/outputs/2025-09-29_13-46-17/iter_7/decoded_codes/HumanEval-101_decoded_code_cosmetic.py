from typing import List


def words_string(obqa: str) -> List[str]:
    def recursiveA8(pos: int, accum: List[str]) -> List[str]:
        if pos >= len(obqa):
            return accum
        curChar = obqa[pos]
        nextAccum = accum + ([' '] if curChar == ',' else [curChar])
        return recursiveA8(pos + 1, nextAccum)

    tabQr = recursiveA8(0, [])

    def splitterXh(acc2: List[str], idx: int) -> List[str]:
        if idx >= len(tabQr):
            return acc2
        ch = tabQr[idx]
        cond1 = ch in (' ', '\t', '\n')
        if cond1 and len(acc2) > 0:
            newAcc = acc2 + [""]
        else:
            newAcc = acc2

        lastIndex = len(newAcc) - 1
        if cond1:
            finalAcc = newAcc
        else:
            prevWord = newAcc[lastIndex]
            finalAcc = newAcc[:lastIndex] + [prevWord + ch]

        return splitterXh(finalAcc, idx + 1)

    if len(obqa) == 0:
        return []
    return splitterXh([""], 0)