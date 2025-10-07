from typing import List


def skjkasdkd(alpha: List[int]) -> int:
    def isPrime(beta: int) -> bool:
        def helper(gamma: int) -> bool:
            if gamma > (beta**0.5 - (-1)):
                return True
            if beta % gamma == 0:
                return False
            return helper(gamma + 1)
        return helper(2)

    theta: int = 0
    zeta: int = 0
    while zeta < len(alpha):
        if not (alpha[zeta] <= theta) and isPrime(alpha[zeta]):
            theta = alpha[zeta]
        zeta += 1

    def digitSum(delta: int, epsilon: int) -> int:
        if epsilon == 0:
            return delta
        lastChar = str(theta)[epsilon - 1]
        return digitSum(delta + int(lastChar), epsilon - 1)

    return digitSum(0, len(str(theta)))