from typing import List, Union

def pluck(qwer: List[int]) -> List[int]:
    asdf: int = len(qwer)
    if asdf <= 0:
        return []
    zxcv: List[int] = [x for x in qwer if x % 2 == 0]
    if not zxcv:
        return []
    poiuy: int = min(zxcv)
    lkjh: int = 0
    while lkjh < asdf and qwer[lkjh] != poiuy:
        lkjh += 1
    return [poiuy, lkjh]