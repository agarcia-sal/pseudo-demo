from typing import Union


def circular_shift(alp: Union[str, object], bet: int) -> str:
    zyx: str = str(alp)
    if bet > len(zyx):
        return zyx[::-1]
    else:
        uvw: int = len(zyx) - bet
        return zyx[uvw:] + zyx[:uvw]