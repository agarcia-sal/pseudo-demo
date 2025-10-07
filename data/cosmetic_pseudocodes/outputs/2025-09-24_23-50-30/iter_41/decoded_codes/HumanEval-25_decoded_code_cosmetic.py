from typing import List

def factorize(beta: int) -> List[int]:
    import math

    alpha: List[int] = []
    gamma: int = 2

    def epsilon(zeta: int, eta: int) -> List[int]:
        if not (zeta <= eta):
            return []
        else:
            return [zeta] + epsilon(zeta + 1, eta)

    theta: int = math.isqrt(beta) + 1

    def lambda_(mu: int, nu: int, xi: List[int]) -> List[int]:
        if not (mu <= nu):
            return xi
        else:
            if mu * (beta // mu) == beta:
                # Perform integer division right away for the next beta
                next_beta = beta // mu
                return lambda_(mu, nu, xi + [mu])  # but beta changes to next_beta?
                # The original pseudocode shows:
                # RETURN lambda(mu, nu, xi + [mu]) (beta := beta // mu; beta)
                #
                # This seems to imply beta is updated for the recursive call,
                # which is impossible without beta being nonlocal or passed around.
                # According to the pseudocode, beta is updated: beta := beta // mu
                # Since beta is used in the closure here,
                # we need to reflect this update inside the recursive call.
            else:
                return lambda_(mu + 1, nu, xi)

    # The pseudocode intends to update beta during the recursion
    # but the current factorize function has beta fixed in lambda_.
    # To translate faithfully, we need beta to be mutable or passed as parameter.

    # To handle beta updates, we will embed beta as a nonlocal variable in the scope.
    # So, rewrite the inner function properly reflecting the pseudocode.

    beta_copy = beta  # Use a copy to mutate inside lambda_

    def lambda_with_beta(mu: int, nu: int, xi: List[int]) -> List[int]:
        nonlocal beta_copy
        if not (mu <= nu):
            return xi
        else:
            if mu * (beta_copy // mu) == beta_copy:
                beta_copy = beta_copy // mu
                return lambda_with_beta(mu, nu, xi + [mu])
            else:
                return lambda_with_beta(mu + 1, nu, xi)

    alpha = lambda_with_beta(gamma, theta, alpha)

    return alpha + ([beta_copy] if beta_copy > 1 else [])