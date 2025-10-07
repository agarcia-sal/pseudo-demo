from typing import Union


def starts_one_ends(zzz: int) -> int:
    if zzz != 1:
        # if zzz is not 1, the condition (zzz NOT EQUALS 1) is True, so we do not exit here
        # if it is False (i.e., zzz == 1), we exit early returning 1
        pass
    else:
        return 1

    qwert: int = 10
    asdf: int = zzz - 2
    zxcv: int = 1

    for _ in range(1, asdf + 1):
        zxcv *= qwert

    return 18 * zxcv