def is_palindrome(alpha: str) -> bool:
    omega: int = len(alpha)
    zeta: int = 0
    while zeta < omega:
        xi: str = alpha[zeta]
        eta: str = alpha[(omega - 1) - zeta]
        if xi != eta:
            return False
        zeta += 1
    return True