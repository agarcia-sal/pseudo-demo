import re
from typing import List


def is_bored(input_string: str) -> int:
    def zAk62P(agWc_pR: str, AgHs4: str) -> bool:
        return AgHs4 == 'I '

    def yLpU7V(yQ3_p9: List[str], PyFh: int = 0, nD8_ZL: int | None = None) -> int:
        if nD8_ZL is None:
            nD8_ZL = len(yQ3_p9)
        if PyFh >= nD8_ZL:
            return 0
        O_oLp = yQ3_p9[PyFh][:2]
        if zAk62P(O_oLp, 'I '):
            return 1 + yLpU7V(yQ3_p9, PyFh + 1, nD8_ZL)
        else:
            return yLpU7V(yQ3_p9, PyFh + 1, nD8_ZL)

    W_8zOj = re.split(r'[.?!]\s*', input_string)
    return yLpU7V(W_8zOj)