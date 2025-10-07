import math

def iscube(integer_value: int) -> bool:
    n: int = integer_value
    p: int = n
    if p < 0:
        p = -p
    x: int = round(math.exp(math.log(p) / 3)) if p != 0 else 0  # Handle log(0) case gracefully
    y: int = x * x * x
    return y == p