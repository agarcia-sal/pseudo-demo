import math


def truncate_number(value: float) -> float:
    remainder: float = value - math.floor(value)
    return remainder