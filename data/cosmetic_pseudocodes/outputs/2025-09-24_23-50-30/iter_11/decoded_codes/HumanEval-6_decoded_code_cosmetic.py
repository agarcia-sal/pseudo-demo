from typing import List

def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        alpha: int = 0  # current depth of open parentheses
        beta: int = 0   # max depth recorded
        idx: int = 0    # index in 0-based Python strings

        while idx < len(group_string):
            ch = group_string[idx]
            if ch == '(':
                alpha += 1
                if beta < alpha:
                    beta = alpha
            else:
                alpha -= 1
            idx += 1
        return beta

    tokens: List[str] = []
    start_pos: int = 0
    end_pos: int = 0
    length = len(parentheses_string)

    while end_pos <= length:
        if end_pos == length or parentheses_string[end_pos] == ' ':
            if end_pos > start_pos:
                tokens.append(parentheses_string[start_pos:end_pos])
            start_pos = end_pos + 1
        end_pos += 1

    result: List[int] = []
    for tok in tokens:
        if len(tok) > 0:
            result.append(parse_paren_group(tok))
    return result