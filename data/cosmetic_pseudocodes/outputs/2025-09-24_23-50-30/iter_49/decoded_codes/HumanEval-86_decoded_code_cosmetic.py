from typing import List

def anti_shuffle(alpha: str) -> str:
    def theta(xi: List[str], omega: int) -> List[str]:
        if omega < len(xi) - 1:
            lambda_char = xi[omega]
            kappa_char = xi[omega + 1]
            if kappa_char < lambda_char:
                xi[omega], xi[omega + 1] = xi[omega + 1], xi[omega]
                return theta(xi, max(0, omega - 1))
            else:
                return theta(xi, omega + 1)
        else:
            return xi

    def mu(beta: List[str]) -> List[str]:
        return theta(beta, 0)

    upsilon = alpha.split(" ")

    def rho(epsilon: int, pi: List[str]) -> List[str]:
        if epsilon == len(upsilon):
            return pi
        chi = mu(list(upsilon[epsilon]))
        phi = "".join(chi)
        return rho(epsilon + 1, pi + [phi])

    omicron = rho(0, [])
    return " ".join(omicron)