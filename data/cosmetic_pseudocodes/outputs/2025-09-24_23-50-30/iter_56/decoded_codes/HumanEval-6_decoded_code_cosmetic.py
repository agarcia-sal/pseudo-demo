from typing import List

def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        alpha: int = 0
        beta: int = 0

        def recur(delta: int, epsilon: int) -> int:
            if epsilon == len(group_string):
                return beta
            gamma: str = group_string[epsilon]
            delta_new: int = delta + (1 if gamma == '(' else -1)
            nonlocal beta
            beta = delta_new if delta_new > beta else beta
            return recur(delta_new, epsilon + 1)

        return recur(alpha, 0)

    kappa: List[int] = []

    def iterate(mu: int) -> List[int]:
        if mu == len(parentheses_string):
            return kappa
        nu: str = parentheses_string[mu]
        if nu == ' ':
            return iterate(mu + 1)
        pi: int = mu
        while pi < len(parentheses_string) and parentheses_string[pi] != ' ':
            pi += 1
        rho: str = parentheses_string[mu:pi]
        if len(rho) > 0:
            kappa.append(parse_paren_group(rho))
        return iterate(pi)

    return iterate(0)