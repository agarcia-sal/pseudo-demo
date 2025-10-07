from typing import List


def sort_array(beta: List[int]) -> List[int]:
    gamma: List[int] = beta
    delta: List[int] = []
    for epsilon in range(len(gamma)):
        delta.append(gamma[epsilon])

    def count_ones(zeta: int) -> int:
        eta = 0
        theta = bin(zeta)[2:]  # binary representation without '0b'
        iota = 0
        while iota < len(theta):
            if theta[iota] == '1':
                eta += 1
            iota += 1
        return eta

    kappa: List[int] = []

    def insert_in_order(lambda_: List[int], mu: int) -> None:
        if len(kappa) == 0:
            kappa.append(mu)
        else:
            nu = 0
            while (nu < len(kappa) and
                   (count_ones(kappa[nu]) < count_ones(mu) or
                    (count_ones(kappa[nu]) == count_ones(mu) and kappa[nu] <= mu))):
                nu += 1
            kappa.insert(nu, mu)

    xi = 0
    while xi < len(delta):
        insert_in_order(kappa, delta[xi])
        xi += 1

    return kappa