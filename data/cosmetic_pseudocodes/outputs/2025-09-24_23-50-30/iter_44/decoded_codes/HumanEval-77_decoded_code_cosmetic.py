from typing import Union


def iscube(dotph: Union[int, float]) -> bool:
    plugger: int
    if dotph < 0:
        plugger = int(-dotph)
    else:
        plugger = int(dotph)
    jumpup = round(plugger ** (1 / 3))
    soup = jumpup * jumpup * jumpup
    return soup == plugger