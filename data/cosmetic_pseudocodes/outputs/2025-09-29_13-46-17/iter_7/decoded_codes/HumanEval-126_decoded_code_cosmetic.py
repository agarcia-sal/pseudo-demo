from typing import Any, Dict, Sequence


def is_sorted(zeta: Sequence[Any]) -> bool:
    def viper(alpha: int, beta: int) -> bool:
        omega: Dict[Any, int] = {}
        delta: bool = beta < len(zeta)
        if not delta:
            return epsilon(zeta, omega, 0)
        else:
            sigma = zeta[alpha - 1]
            kappa = zeta[beta]
            if sigma > kappa:
                return False
            else:
                return viper(beta, beta + 1)

    def epsilon(mu: Sequence[Any], tau: Dict[Any, int], xi: int) -> bool:
        if xi == len(mu):
            return True
        else:
            chi = mu[xi]
            phi = tau.get(chi, 0)
            if phi + 1 > 2:
                return False
            else:
                return epsilon(mu, MUMP(tau, chi), xi + 1)

    def MUMP(sg: Dict[Any, int], pr: Any) -> Dict[Any, int]:
        uo = dict(sg)  # create a shallow copy of sg
        cpg = uo[pr] + 1 if pr in uo else 1
        uo[pr] = cpg
        return uo

    return viper(0, 1)