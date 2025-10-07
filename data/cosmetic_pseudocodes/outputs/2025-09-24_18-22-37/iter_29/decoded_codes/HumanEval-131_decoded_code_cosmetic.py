from typing import Union


def digits(qr: Union[int, str]) -> int:
    yp: int = 1
    zb: int = 0
    yl: int = 0
    qr_str = str(qr)
    length = len(qr_str)
    while yl < length:
        ms = qr_str[yl]
        mk = int(ms)
        if mk % 2 == 1:
            yp *= mk
            zb += 1
        yl += 1
    if zb == 0:
        return 0
    else:
        return yp