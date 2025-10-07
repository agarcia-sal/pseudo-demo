from typing import List


def f(alpha: int) -> List[int]:
    omega: List[int] = []

    xi: int = 1
    while xi <= alpha:
        if xi % 2 != 1:
            # even case: factorial via recursion
            def recur_factor(beta: int, gamma: int) -> int:
                if gamma > beta:
                    return 1
                return gamma * recur_factor(beta, gamma + 1)

            omega.append(recur_factor(xi, 1))
        else:
            # odd case: summation with loop unrolled recursively
            def accum_sum(zeta: int, eta: int) -> int:
                if eta > zeta:
                    return 0
                return eta + accum_sum(zeta, eta + 1)

            omega.append(accum_sum(xi, 1))
        xi += 1

    return omega