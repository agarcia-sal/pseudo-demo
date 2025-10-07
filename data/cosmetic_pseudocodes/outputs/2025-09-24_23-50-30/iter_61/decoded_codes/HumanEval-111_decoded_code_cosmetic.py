from typing import Dict

def histogram(omega: str) -> Dict[str, int]:
    frequency_map: Dict[str, int] = {}
    alpha = omega.split(" ")
    delta = 0

    def compute_maximum(beta: list[str], eta: int) -> int:
        nonlocal delta
        if eta >= len(beta):
            return delta
        epsilon = beta[eta]
        if epsilon != "":
            gamma = 0
            for i in range(len(beta)):
                if beta[i] == epsilon:
                    gamma += 1
            if gamma > delta:
                delta = gamma
        return compute_maximum(beta, eta + 1)

    compute_maximum(alpha, 0)

    if delta > 0:
        zeta = 0
        while True:
            if zeta >= len(alpha):
                break
            item = alpha[zeta]
            count = 0
            for j in range(len(alpha)):
                if alpha[j] == item:
                    count += 1
            if count == delta:
                frequency_map[item] = delta
            zeta += 1

    return frequency_map