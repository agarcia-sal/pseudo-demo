from typing import List


def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        alpha: int = 0
        beta: int = 0
        epsilon: int = 0
        length: int = len(group_string)
        while epsilon < length:
            phi: str = group_string[epsilon]
            if phi == '(':
                alpha += 1
                if alpha > beta:
                    beta = alpha
            else:
                alpha -= 1
            epsilon += 1
        return beta

    omega: List[str] = parentheses_string.split(' ')
    gamma: List[int] = []
    delta: int = 0
    while delta < len(omega):
        sigma: str = omega[delta]
        if sigma != '':
            psi: int = parse_paren_group(sigma)
            gamma.append(psi)
        delta += 1

    return gamma