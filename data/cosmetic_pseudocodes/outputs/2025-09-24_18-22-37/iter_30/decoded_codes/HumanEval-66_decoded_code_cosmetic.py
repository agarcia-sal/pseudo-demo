def digitSum(omega: str) -> int:
    if omega == "":
        return 0
    total: int = 0
    for zeta in omega:
        if 'A' <= zeta <= 'Z':
            tempVal: int = ord(zeta)
        else:
            tempVal = 0
        total += tempVal
    return total