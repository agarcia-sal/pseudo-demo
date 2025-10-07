from typing import Optional, Union


def digits(lambda_: Union[int, str]) -> int:
    tau: int = 1
    kappa: int = 0

    def loop(mu: int, sigma: int, rho: Optional[str]) -> int:
        if rho is None:
            return 0 if kappa == 0 else tau
        if not rho:
            # Empty string treated same as None per pseudocode logic (not explicit, but reasonable)
            return 0 if kappa == 0 else tau

        omega: int = int(rho[0])
        psi: int = mu
        chi: int = sigma

        if omega % 2 != 1:
            return loop(psi, chi, rho[1:])
        else:
            psi = mu * omega
            chi = sigma + 1
            return loop(psi, chi, rho[1:])

    return loop(tau, kappa, str(lambda_))