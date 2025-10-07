from typing import List

def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        alpha = 0
        beta = 0
        index = 0
        length = len(group_string)
        while index < length:
            char_x = group_string[index]
            if char_x == '(':
                alpha += 1
                beta = alpha if alpha > beta else beta
            else:
                alpha -= 1
            index += 1
        return beta

    omega: List[int] = []
    tokens: List[str] = []
    length_s = len(parentheses_string)
    start_pos = 0

    for iterator in range(length_s):
        c = parentheses_string[iterator]
        if c == ' ':
            if iterator > start_pos:
                tokens.append(parentheses_string[start_pos:iterator])
            start_pos = iterator + 1
    if start_pos < length_s:
        tokens.append(parentheses_string[start_pos:length_s])

    acc: List[int] = []
    for elem in tokens:
        if len(elem) > 0:
            acc.append(parse_paren_group(elem))

    return acc