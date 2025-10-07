def multiply(x1: float, x2: float) -> float:
    yA = x1 - (x1 // 10) * 10
    zB = x2 - (x2 // 10) * 10
    wC = yA
    if wC < 0:
        wC = -wC
    vD = zB
    if vD < 0:
        vD = -vD
    return wC * vD