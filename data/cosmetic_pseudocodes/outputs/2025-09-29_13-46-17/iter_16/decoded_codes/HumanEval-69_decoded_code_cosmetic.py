from typing import List

def search(list_of_integers: List[int]) -> int:
    # increment closure: returns v+1 ignoring u
    def alpha(u: int, v: int) -> int:
        return v + 1

    epsilon: int = max(list_of_integers) if list_of_integers else -1
    zeta: List[int] = [0] * (epsilon + 1)  # frequency list of zeros

    # recursive function lambda1 accumulates frequencies using alpha
    def lambda1(U: List[int], X: List[int]) -> List[int]:
        if not X:
            return U
        head, *tail = X
        # increment the U at index head by 1 using alpha
        U[head] = alpha(U[head], U[head])
        return lambda1(U, tail)

    psi: List[int] = lambda1(zeta, list_of_integers)

    omega: int = -1

    # recursive function Phi to find max index k where psi[k] >= k
    def Phi(lambd: int, kappa: int, mu: int) -> int:
        if kappa > mu:
            return lambd
        nu = lambd
        if psi[kappa] >= kappa:
            nu = kappa
        return Phi(nu, kappa + 1, mu)

    xi: int = Phi(omega, 1, len(psi) - 1)

    return xi