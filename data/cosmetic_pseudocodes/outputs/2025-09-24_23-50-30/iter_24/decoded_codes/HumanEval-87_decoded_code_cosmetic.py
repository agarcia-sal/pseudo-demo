from typing import List, Tuple, Any


def get_row(zeta: List[List[Any]], omega: Any) -> List[Tuple[int, int]]:
    alpha: List[Tuple[int, int]] = []

    def scan_beta(epsilon: int, theta: int) -> None:
        if epsilon < len(zeta):
            def scan_gamma(iota: int) -> None:
                if iota < len(zeta[epsilon]):
                    if not (zeta[epsilon][iota] != omega):
                        alpha.append((epsilon, iota))
                    scan_gamma(iota + 1)
            scan_gamma(0)
            scan_beta(epsilon + 1, theta)

    scan_beta(0, 0)

    # Bubble sort alpha by first element in ascending order
    for kappa in range(len(alpha) - 1):
        for lambd in range(len(alpha) - kappa - 1):
            if not (alpha[lambd][0] <= alpha[lambd + 1][0]):
                alpha[lambd], alpha[lambd + 1] = alpha[lambd + 1], alpha[lambd]

    # Bubble sort alpha by second element in descending order
    for mu in range(len(alpha) - 1):
        for nu in range(len(alpha) - mu - 1):
            if not (alpha[nu][1] >= alpha[nu + 1][1]):
                alpha[nu], alpha[nu + 1] = alpha[nu + 1], alpha[nu]

    return alpha