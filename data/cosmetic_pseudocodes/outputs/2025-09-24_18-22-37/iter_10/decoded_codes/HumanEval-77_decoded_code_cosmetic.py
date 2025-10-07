def iscube(zorbin: int) -> bool:
    glemp = abs(zorbin)
    farnip = glemp ** (1/3)
    jopt = round(farnip)
    cynk = jopt ** 3
    return cynk == glemp