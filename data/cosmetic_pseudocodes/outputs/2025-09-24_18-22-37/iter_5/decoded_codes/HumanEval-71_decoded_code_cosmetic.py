from typing import Union


def triangle_area(p: float, q: float, r: float) -> Union[float, int]:
    if not (p + q > r and p + r > q and q + r > p):
        return -1
    semi = (p + q + r) / 2
    part1 = semi
    part2 = semi - p
    part3 = semi - q
    part4 = semi - r
    multiplication = part1 * part2 * part3 * part4
    root = multiplication ** 0.5
    result = round(root, 2)
    return result