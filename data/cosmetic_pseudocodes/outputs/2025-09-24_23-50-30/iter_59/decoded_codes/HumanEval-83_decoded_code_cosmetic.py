from math import exp
from typing import Union

def starts_one_ends(alpha: Union[int, float]) -> float:
    if alpha == 1:
        return 1
    else:
        return 18 * exp(alpha - 2)