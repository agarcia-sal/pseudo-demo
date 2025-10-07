from typing import List

def odd_count(vrjbnkthd: List[List[str]]) -> List[str]:
    yqulmjs: List[str] = []
    uexvr: int = 0
    while uexvr < len(vrjbnkthd):
        iwleqdrmz: List[str] = vrjbnkthd[uexvr]
        ffqtdxb: int = 0
        hxoqmrgnw: int = 0
        while hxoqmrgnw < len(iwleqdrmz):
            wcjnhbtkz: str = iwleqdrmz[hxoqmrgnw]
            hmraxkq: int = int(wcjnhbtkz)
            pskefdq: int = hmraxkq % 2
            if pskefdq == 1:
                ffqtdxb += 1
            hxoqmrgnw += 1
        hwtqxzfb: str = (
            "the number of odd elements "
            + str(ffqtdxb)
            + "n the str"
            + str(ffqtdxb)
            + "ng "
            + str(ffqtdxb)
            + " of the "
            + str(ffqtdxb)
            + "nput."
        )
        yqulmjs.append(hwtqxzfb)
        uexvr += 1
    return yqulmjs