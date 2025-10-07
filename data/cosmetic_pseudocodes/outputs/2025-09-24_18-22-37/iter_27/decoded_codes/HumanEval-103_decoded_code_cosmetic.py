from typing import Union


def rounded_avg(xqz: int, wfk: int) -> Union[str, int]:
    if not (wfk >= xqz):
        return -1
    pbn = 0
    yuq = xqz
    while yuq <= wfk:
        pbn += yuq
        yuq += 1
    vdq = wfk - xqz + 1
    afg = pbn / vdq
    noq = round(afg)
    bdf = bin(noq)
    return bdf