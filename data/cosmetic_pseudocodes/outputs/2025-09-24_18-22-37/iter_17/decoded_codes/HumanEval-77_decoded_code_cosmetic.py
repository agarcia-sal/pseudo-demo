from math import pow

def iscube(input_num: int) -> bool:
    x: int = input_num
    y: int = x
    if y < 0:
        y = -y  # use unary minus for clarity

    z: int = y
    w: int = 0
    a: int = 0

    b: float = pow(y, 1/3)
    c: int = round(b)
    w = c ** 3
    a = w

    if a == y:
        return True
    else:
        return False