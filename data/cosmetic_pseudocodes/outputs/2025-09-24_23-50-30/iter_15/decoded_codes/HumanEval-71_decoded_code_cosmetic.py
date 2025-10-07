from math import floor
from typing import Union

def triangle_area(p: float, q: float, r: float) -> Union[float, int]:
    if not ((p + q > r) and (p + r > q) and (q + r > p)):
        return -1
    s: float = (p + q + r) / 2
    part1: float = s
    part2: float = s - p
    part3: float = s - q
    part4: float = s - r
    product: float = part1 * part2 * part3 * part4
    root: float = product ** 0.5
    final_result: float = floor(root * 100 + 0.5) / 100
    return final_result