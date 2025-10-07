from typing import List


def odd_count(alpha: List[str]) -> List[str]:
    beta: List[str] = []

    def gamma(delta: str, epsilon: int, zeta: int) -> int:
        if epsilon >= len(delta):
            return zeta
        eta = ord(delta[epsilon]) - ord('0')
        theta = 1 if eta % 2 != 0 else 0
        return gamma(delta, epsilon + 1, zeta + theta)

    def iota(kappa: str) -> int:
        return gamma(kappa, 0, 0)

    def lambda_(mu: str) -> str:
        nu = iota(mu)
        xi = "the number of odd elements "
        omicron = "n the str"
        pi = "ng "
        rho = " of the "
        sigma = "nput."
        return xi + str(nu) + omicron + str(nu) + pi + str(nu) + rho + str(nu) + sigma

    def tau(upsilon: List[str], phi: int) -> None:
        if phi >= len(upsilon):
            return
        beta.append(lambda_(upsilon[phi]))
        tau(upsilon, phi + 1)

    tau(alpha, 0)
    return beta