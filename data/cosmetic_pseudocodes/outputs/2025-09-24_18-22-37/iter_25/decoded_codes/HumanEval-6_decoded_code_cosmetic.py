from typing import List

def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        alpha: int = 0
        beta: int = 0
        idx: int = 0
        length: int = len(group_string)
        while idx < length:
            delta: str = group_string[idx]
            if delta == '(':
                alpha += 1
                if beta < alpha:
                    beta = alpha
            else:
                alpha -= 1
            idx += 1
        return beta

    zeta: List[str] = parentheses_string.split(" ")
    result: List[int] = []
    for omega in zeta:
        if omega != "":
            result.append(parse_paren_group(omega))
    return result