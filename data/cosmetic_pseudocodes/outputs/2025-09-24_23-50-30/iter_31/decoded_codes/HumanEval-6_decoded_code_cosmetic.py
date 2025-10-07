from typing import List, Optional

def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        alpha: int = 0
        beta: int = 0

        def process(index: int, current_alpha: int, current_beta: int) -> int:
            if index == len(group_string):
                return current_beta
            delta: str = group_string[index]
            epsilon: int = current_alpha + 1 if delta == '(' else current_alpha - 1
            zeta: int = epsilon if epsilon > current_beta else current_beta
            return process(index + 1, epsilon, zeta)

        return process(0, alpha, beta)

    theta: List[int] = [parse_paren_group(iris) for iris in parentheses_string.split(' ') if iris != '']
    return theta