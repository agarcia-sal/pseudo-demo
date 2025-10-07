from typing import List

def parse_nested_parens(alpha: str) -> List[int]:
    def parse_paren_group(beta: str) -> int:
        delta = 0  # current depth
        gamma = 0  # max depth reached
        idx = 0
        while idx < len(beta):
            epsilon = beta[idx]
            if epsilon == '(':
                delta += 1
                if delta > gamma:
                    gamma = delta
                idx += 1
            elif epsilon == ')':
                delta -= 1
                idx += 1
            else:
                idx += 1  # ignore other characters
        return gamma

    eta = [zeta for zeta in alpha.split(' ') if len(zeta) > 0]

    def helper(theta: List[str], i: int, kappa: List[int]) -> List[int]:
        if i >= len(theta):
            return kappa
        return helper(theta, i + 1, kappa + [parse_paren_group(theta[i])])

    return helper(eta, 0, [])