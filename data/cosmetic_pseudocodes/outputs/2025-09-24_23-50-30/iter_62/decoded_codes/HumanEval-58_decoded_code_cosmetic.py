from typing import Iterable, List, Set, TypeVar

T = TypeVar('T')

def common(omega: Iterable[T], psi: Iterable[T]) -> List[T]:
    def recur_alpha(zeta: Iterable[T], eta: Iterable[T], theta: Set[T]) -> Set[T]:
        zeta_iter = iter(zeta)
        try:
            lambda_ = next(zeta_iter)
        except StopIteration:
            return theta
        mu = recur_beta(psi, lambda_, theta)
        # Recurse with the rest of zeta; pass eta unchanged as per pseudocode
        return recur_alpha(zeta_iter, eta, mu)

    def recur_beta(nu: Iterable[T], xi: T, sigma: Set[T]) -> Set[T]:
        nu_iter = iter(nu)
        try:
            rho = next(nu_iter)
        except StopIteration:
            return sigma
        tau = sigma
        if xi == rho:
            tau = sigma | {xi}
        # Recurse with rest of nu
        return recur_beta(nu_iter, xi, tau)

    epsilon = recur_alpha(omega, psi, set())
    phi = list(epsilon)
    kappa = sorted(phi)
    return kappa