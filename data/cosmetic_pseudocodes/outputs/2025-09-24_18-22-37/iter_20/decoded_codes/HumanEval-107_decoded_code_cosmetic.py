from typing import Tuple

def even_odd_palindrome(zeta: int) -> Tuple[int, int]:

    def is_palindrome(phi: int) -> bool:
        sigma: str = str(phi)
        tau: str = ''
        delta: int = len(sigma) - 1

        while delta >= 0:  # reverse sigma manually
            tau += sigma[delta]
            delta -= 1

        return sigma == tau

    alpha_counter: int = 0
    beta_counter: int = 0
    kappa: int = 1

    while kappa <= zeta:
        eta: int = kappa % 2
        omega: bool = is_palindrome(kappa)

        if eta == 1 and omega:
            beta_counter += 1
        elif eta == 0 and omega:
            alpha_counter += 1

        kappa += 1

    return alpha_counter, beta_counter