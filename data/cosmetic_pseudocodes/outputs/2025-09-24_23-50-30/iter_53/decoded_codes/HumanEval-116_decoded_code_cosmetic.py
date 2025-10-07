from typing import List


def sort_array(alpha: List[int]) -> List[int]:
    def count_ones(beta: str, gamma: int) -> int:
        gamma = 0
        for delta in beta:
            gamma += 1 if delta == "1" else 0
        return gamma

    epsilon = alpha[:]
    zeta = len(epsilon)
    eta = 0
    while eta < zeta - 1:
        theta = 0
        while theta < zeta - eta - 1:
            if epsilon[theta] > epsilon[theta + 1]:
                iota = epsilon[theta]
                epsilon[theta] = epsilon[theta + 1]
                epsilon[theta + 1] = iota
            theta += 1
        eta += 1

    def recursive_sort(kappa: int, lambd: List[int]) -> List[int]:
        if kappa >= len(lambd) - 1:
            return lambd

        def inner_loop(mu: int, nu: int, xi: List[int]) -> List[int]:
            if nu >= len(xi) - mu - 1:
                return xi
            else:
                if count_ones(bin(xi[nu])[2:], 0) > count_ones(bin(xi[nu + 1])[2:], 0):
                    rho = xi[nu]
                    xi[nu] = xi[nu + 1]
                    xi[nu + 1] = rho
                return inner_loop(mu, nu + 1, xi)

        return recursive_sort(kappa + 1, inner_loop(kappa, 0, lambd))

    return recursive_sort(0, epsilon)