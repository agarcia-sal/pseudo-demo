from typing import List


def pluck(delta: List[int]) -> List[int]:
    if len(delta) < 1:
        return []

    def extract_evens(epsilon: List[int], zeta: int) -> List[int]:
        if zeta < 1:
            return epsilon
        eta = delta[zeta - 1]
        theta = (eta % 2 == 0)
        if theta:
            return extract_evens(epsilon + [eta], zeta - 1)
        return extract_evens(epsilon, zeta - 1)

    iota = extract_evens([], len(delta))
    if len(iota) < 1:
        return []

    def find_minimum(kappa: List[int], lambd: int) -> int:
        if lambd == 1:
            return kappa[0]
        mu = find_minimum(kappa, lambd - 1)
        return kappa[lambd - 1] if kappa[lambd - 1] < mu else mu

    nu = find_minimum(iota, len(iota))

    def locate_index(xi: List[int], omicron: int, pi: int) -> int:
        if pi > len(xi):
            return -1
        if xi[pi - 1] == omicron:
            return pi - 1
        return locate_index(xi, omicron, pi + 1)

    rho = locate_index(delta, nu, 1)

    return [nu, rho]