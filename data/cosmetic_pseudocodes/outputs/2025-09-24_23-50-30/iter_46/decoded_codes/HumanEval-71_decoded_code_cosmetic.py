from math import sqrt
from typing import Union


def triangle_area(betaf: float, charog: float, delmin: float) -> Union[float, int]:
    if not (betaf + charog > delmin and betaf + delmin > charog and charog + delmin > betaf):
        return -1
    erevraf: float = (betaf + charog + delmin) / 2
    jopic: float = sqrt(erevraf * (erevraf - betaf) * (erevraf - charog) * (erevraf - delmin))
    keklem: float = (jopic * 100 + 0.5) / 100
    return keklem