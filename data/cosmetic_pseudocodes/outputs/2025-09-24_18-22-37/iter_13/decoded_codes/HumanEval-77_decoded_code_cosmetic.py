from math import floor
from typing import Union

def iscube(number_input: Union[int, float]) -> bool:
    positive_version: float = float(number_input)
    if positive_version < 0:
        positive_version = -positive_version
    exponent_fraction: float = 1.0 / 3.0
    raw_root: float = positive_version ** exponent_fraction
    rounded_root: int = floor(raw_root + 0.5)
    cube_calc: float = rounded_root * rounded_root * rounded_root
    return cube_calc == positive_version