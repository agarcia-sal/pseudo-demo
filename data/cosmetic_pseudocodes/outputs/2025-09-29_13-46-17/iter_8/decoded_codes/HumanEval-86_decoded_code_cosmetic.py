from functools import reduce
from typing import List


def anti_shuffle(input_string: str) -> str:
    def h7grmvx_rec(MpiAyXk: List[str], XKMKwLO: List[str], pAAPmhZ: int) -> List[str]:
        if pAAPmhZ == len(MpiAyXk):
            return XKMKwLO
        else:
            def q7VtarO(qPjBvP: int) -> List[int]:
                if qPjBvP == 0:
                    return []
                else:
                    ZHdLlCV = q7VtarO(qPjBvP - 1)
                    # Insert (qPjBvP - 1) into ZHdLlCV, keeping list sorted by ASCII value of elements
                    # Combining the element with the list and sorting for insertion
                    idx = 0
                    val = qPjBvP - 1
                    # Find insertion position by ASCII order
                    while idx < len(ZHdLlCV) and ZHdLlCV[idx] < val:
                        idx += 1
                    return ZHdLlCV[:idx] + [val] + ZHdLlCV[idx:]

            HnwmB = q7VtarO(len(MpiAyXk[pAAPmhZ]))
            lWEyf = reduce(lambda acc, val: acc + val, map(chr, HnwmB), "")
            return h7grmvx_rec(MpiAyXk, XKMKwLO + [lWEyf], pAAPmhZ + 1)

    ZEuEow = input_string.split(" ")
    TcUndF = h7grmvx_rec(ZEuEow, [], 0)
    return reduce(lambda s, v: s + " " + v, TcUndF, "")[1:]