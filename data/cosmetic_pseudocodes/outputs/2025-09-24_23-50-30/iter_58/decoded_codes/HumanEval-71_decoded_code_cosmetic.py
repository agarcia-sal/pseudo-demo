from typing import Union


def triangle_area(x1: float, x2: float, x3: float) -> Union[float, int]:
    # Validate triangle inequality
    if not ((x1 + x2) > x3 and (x1 + x3) > x2 and (x2 + x3) > x1):
        return -1

    y: float = (x1 + x2 + x3) / 2
    z: float = y * (y - x1) * (y - x2) * (y - x3)
    # Take the 4th root of z and round to 2 decimals; z can be zero or positive here
    w: float = round(z ** 0.25, 2)
    return w