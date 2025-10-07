from typing import List

def hex_key(beta: str) -> int:
    omega: List[str] = ['2', '3', '5', '7', 'B', 'D']

    def zeta(epsilon: int, theta: int) -> int:
        if theta < len(beta):
            if beta[theta] in omega:
                return zeta(epsilon + 1, theta + 1)
            else:
                return zeta(epsilon, theta + 1)
        else:
            return epsilon

    return zeta(0, 0)