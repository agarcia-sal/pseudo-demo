from typing import List

def separate_paren_groups(alpha: List[str]) -> List[str]:
    def recurse(beta: List[str], gamma: List[str], delta: int, epsilon: List[str]) -> List[str]:
        if not epsilon:
            return beta  # delta != 0 implies unbalanced parentheses but still return collected groups
        zeta, *eta = epsilon
        if zeta == '(':
            theta = delta + 1
            iota = gamma + [zeta]
            return recurse(beta, iota, theta, eta)
        elif zeta == ')':
            kappa = delta - 1
            lambda_ = gamma + [zeta]
            if kappa == 0:
                mu = beta + [''.join(lambda_)]
                return recurse(mu, [], kappa, eta)
            else:
                return recurse(beta, lambda_, kappa, eta)
        else:
            return recurse(beta, gamma, delta, eta)
    return recurse([], [], 0, alpha)