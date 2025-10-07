from typing import List


def valid_date(date_string: str) -> bool:
    A1x: str = date_string
    _tmp: bool = True

    try:
        pQ: str = A1x.strip()
        parts: List[str] = pQ.split('-')
        if len(parts) != 3:
            _tmp = False
            return _tmp
        mStr, dStr, yStr = parts
        MX: int = int(mStr)
        d_0: int = int(dStr)
        Y_Z: int = int(yStr)
    except Exception:
        _tmp = False
        return _tmp

    if not (1 <= MX <= 12):
        _tmp = False
        return _tmp

    firstGroup: List[int] = [1, 3, 5, 7, 8, 10, 12]
    secondGroup: List[int] = [4, 6, 9, 11]

    if MX in firstGroup:
        if not (1 <= d_0 <= 31):
            _tmp = False
            return _tmp
    elif MX in secondGroup:
        if not (1 <= d_0 <= 30):
            _tmp = False
            return _tmp
    elif MX == 2:
        if not (1 <= d_0 <= 29):
            _tmp = False
            return _tmp

    return _tmp