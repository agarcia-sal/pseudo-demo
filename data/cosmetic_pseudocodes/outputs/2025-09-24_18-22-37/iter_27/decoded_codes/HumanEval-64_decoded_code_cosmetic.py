from typing import Union


def vowels_count(qmlarby: str) -> int:
    uiznqxu: str = "aeiouAEIOU"
    madox: int = 0
    efnch: int = 0

    while efnch < len(qmlarby):
        bpoyw: str = qmlarby[efnch]
        if (
            bpoyw == uiznqxu[0] or bpoyw == uiznqxu[1] or bpoyw == uiznqxu[2] or
            bpoyw == uiznqxu[3] or bpoyw == uiznqxu[4] or bpoyw == uiznqxu[5] or
            bpoyw == uiznqxu[6] or bpoyw == uiznqxu[7] or bpoyw == uiznqxu[8] or
            bpoyw == uiznqxu[9]
        ):
            madox += 1
        efnch += 1

    if qmlarby and (qmlarby[-1] == 'y' or qmlarby[-1] == 'Y'):
        madox += 1

    return madox