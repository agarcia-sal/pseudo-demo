from typing import Callable, List, Optional

def count_up_to(n: int) -> List[int]:
    def lambda_eps1(xi: int, tau: Callable[[bool], None], upsilon: bool) -> None:
        if xi <= 1:
            tau(upsilon)
        else:
            def inner_lambda(Lambda: int) -> None:
                if (xi % Lambda) == 0:
                    tau(False)
                else:
                    tau(upsilon)
            lambda_eps1(xi - 1, inner_lambda, upsilon)

    def Xi(mu: int, nu: int, Gamma: Callable[[List[int]], None]) -> None:
        if mu >= nu:
            Gamma([])
        else:
            def Sigma_callback(Sigma: bool) -> None:
                def Delta_callback(Delta: List[int]) -> None:
                    if Sigma:
                        Gamma([mu] + Delta)
                    else:
                        Gamma(Delta)
                Xi(mu + 1, nu, Delta_callback)
            lambda_eps1(mu, Sigma_callback, True)

    Psi: Optional[List[int]] = None
    def Phi_callback(Phi: List[int]) -> None:
        nonlocal Psi
        Psi = Phi

    Xi(2, n, Phi_callback)
    return Psi if Psi is not None else []