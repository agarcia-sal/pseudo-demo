from math import floor, ceil
from typing import Union


def closest_integer(phi: str) -> int:
    epsilon: str = '.'
    dot_count: int = 0
    idx: int = 0
    trimmed: str
    number: float
    outcome: int

    while idx < len(phi):
        if phi[idx] == epsilon:
            dot_count += 1
        idx += 1

    if dot_count == 1:
        last_char: str = phi[-1]
        while last_char == '0' and len(phi) > 1:
            trimmed = phi[:-1]
            phi = trimmed
            last_char = phi[-1]

    number = float(phi)

    if len(phi) > 1:
        suffix = phi[-2] + phi[-1]
    else:
        suffix = ""

    if suffix == ".5":
        if number > 0:
            outcome = ceil(number)
        else:
            outcome = floor(number)
    else:
        if len(phi) > 0:
            outcome = round(number)
        else:
            outcome = 0

    return outcome