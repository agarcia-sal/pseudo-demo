def digitSum(alpha: str) -> int:
    theta: int = 0
    iota: int = 0
    while iota < len(alpha):
        kappa: str = alpha[iota]
        if 'A' <= kappa <= 'Z':
            theta += ord(kappa)
        iota += 1
    return theta