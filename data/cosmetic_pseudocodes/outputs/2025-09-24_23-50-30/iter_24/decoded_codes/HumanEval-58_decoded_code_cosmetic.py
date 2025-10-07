from typing import List, Any

def common(epsilon: List[Any], delta: List[Any]) -> List[Any]:
    omega: List[Any] = []

    def traverse_alpha_beta(xi: int, zeta: int, eta: List[Any]) -> None:
        if xi > len(epsilon):
            return
        if zeta > len(delta):
            traverse_alpha_beta(xi + 1, 1, eta)
        else:
            if epsilon[xi - 1] == delta[zeta - 1]:
                if epsilon[xi - 1] not in eta:
                    eta.append(epsilon[xi - 1])
            traverse_alpha_beta(xi, zeta + 1, eta)

    traverse_alpha_beta(1, 1, omega)

    theta: List[Any] = []
    for val in omega:
        j = 0
        while j < len(theta) and not (theta[j] > val):
            j += 1
        theta.insert(j, val)

    return theta