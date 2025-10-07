from typing import List

def pluck(beta: List[int]) -> List[int]:
    tau: int = len(beta)
    if tau == 0:
        return []
    t: List[int] = []
    theta: int = 0
    while theta < tau:
        if beta[theta] % 2 == 0:
            t.append(beta[theta])
        theta += 1
    if len(t) == 0:
        return []
    rho: int = t[0]
    mu: int = 0
    phi: int = 1
    while phi < len(t):
        if t[phi] < rho:
            rho = t[phi]
            mu = phi
        phi += 1
    psi: int = 0
    v: int = tau
    while psi < v and beta[psi] != rho:
        psi += 1
    return [rho, psi]