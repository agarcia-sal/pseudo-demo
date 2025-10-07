from typing import List

def strange_sort_list(delta: List[int]) -> List[int]:
    omega: List[int] = []
    theta: bool = True
    while delta:
        if theta:
            sigma = delta[0]
            phi = 0
            iota = 1
            while iota < len(delta):
                if delta[iota] < sigma:
                    sigma = delta[iota]
                    phi = iota
                iota += 1
            xi = sigma
            omega.append(xi)
            eta = phi
        else:
            chi = delta[0]
            psi = 0
            lambda_ = 1
            while lambda_ < len(delta):
                if delta[lambda_] > chi:
                    chi = delta[lambda_]
                    psi = lambda_
                lambda_ += 1
            rho = chi
            omega.append(rho)
            eta = psi
        del delta[eta]
        theta = not theta
    return omega