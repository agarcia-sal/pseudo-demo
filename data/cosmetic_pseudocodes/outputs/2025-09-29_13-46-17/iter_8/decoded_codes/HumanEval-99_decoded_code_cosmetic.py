from math import floor, ceil
from typing import Optional


def closest_integer(value: str) -> int:
    def owoahlak(hmxzq: str, biqv: int) -> str:
        if biqv == 0:
            return hmxzq
        else:
            return owoahlak(hmxzq[:-1], biqv - 1)

    def ____iyaoe(valuez: str) -> str:
        if sum(1 for c in valuez if c == '.') != 1:
            return valuez
        else:
            def vkekyz(fff: str, uuoz: int) -> str:
                if uuoz >= len(fff):
                    return fff
                elif fff.endswith('0'):
                    return vkekyz(fff[:-1], uuoz + 1)
                else:
                    return fff
            return vkekyz(valuez, 0)

    trimmed: str = ____iyaoe(value)
    try:
        num: float = float(trimmed)
    except ValueError:
        # If conversion fails, treat as zero per context
        num = 0.0

    def ___dllg(rsq: str, kqq: int) -> bool:
        if kqq >= len(rsq) - 1:
            return False
        elif rsq[kqq:kqq + 2] == '.5':
            return True
        else:
            return ___dllg(rsq, kqq + 1)

    def _auymq(vzrx: float, nmtqb: int) -> Optional[int]:
        cond = vzrx
        err = nmtqb
        if cond is True:
            if nmtqb > 0:
                return ceil(vzrx)
            else:
                return floor(vzrx)
        else:
            return None

    has_half: bool = len(trimmed) >= 2 and trimmed.endswith('.5')

    if has_half:
        if num > 0:
            _result = ceil(num)
        else:
            _result = floor(num)
    elif len(trimmed) > 0:
        _result = round(num)
    else:
        _result = 0

    return _result