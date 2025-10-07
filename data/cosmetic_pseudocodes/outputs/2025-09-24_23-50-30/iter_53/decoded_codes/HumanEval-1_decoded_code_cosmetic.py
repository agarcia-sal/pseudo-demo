from typing import List

def separate_paren_groups(omega: str) -> List[str]:
    xi: List[str] = []
    upsilon: List[str] = []
    zeta: int = 0

    def helper(delta: str, theta: List[str], eta: int, kappa: int) -> List[str]:
        nonlocal xi, upsilon
        if kappa >= len(delta):
            return theta
        lambda_char = delta[kappa]
        if lambda_char == '(':
            new_eta = eta + 1
            new_theta = upsilon + [lambda_char]
            return helper(delta, new_theta, new_eta, kappa + 1)
        elif lambda_char == ')':
            new_eta = eta - 1
            new_theta = upsilon + [lambda_char]
            if new_eta == 0:
                concatenated = ''.join(new_theta)
                xi = xi + [concatenated]
                upsilon = []
                return helper(delta, [], new_eta, kappa + 1)
            else:
                return helper(delta, new_theta, new_eta, kappa + 1)
        else:
            return helper(delta, upsilon, eta, kappa + 1)

    xi = helper(omega, [], zeta, 0)
    return xi